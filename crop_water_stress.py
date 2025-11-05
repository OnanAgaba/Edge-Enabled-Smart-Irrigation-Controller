# Crop Water Stress Detection Using CNN on Raspberry Pi 5

# This program captures thermal images from an MLX90640 camera, reads
# soil moisture and environmental sensors, calculates CWSI and SMSI,
# and uses a Convolutional Neural Network to detect crop water stress
# in real-time. The system can automatically trigger irrigation via a solenoid valve.
# Author: Onan Agaba
# First Created: September 09, 2025
# Last Modified: November 05, 2025


import time
import numpy as np
import RPi.GPIO as GPIO
import busio
import board
import adafruit_mlx90640
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import img_to_array


# GPIO setup for solenoid valve
SOLENOID_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOLENOID_PIN, GPIO.OUT)
GPIO.output(SOLENOID_PIN, GPIO.LOW)


# MLX90640 Thermal Camera Setup
i2c = busio.I2C(board.SCL, board.SDA, frequency=400000)
mlx = adafruit_mlx90640.MLX90640(i2c)
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ


# Placeholder functions for other sensors
def read_dht22():
    temp = 30.0  # °C
    rh = 60.0    # %
    return temp, rh

def read_tdr():
    soil_moisture = 0.25  # fraction
    return soil_moisture

# Crop Water Stress Index
def calculate_cwsi(canopy_temp, air_temp, rh):
    Tc_max = air_temp + (1 - rh/100)*10
    cwsi = (canopy_temp - air_temp) / (Tc_max - air_temp)
    cwsi = np.clip(cwsi, 0, 1)
    return cwsi

# Soil Moisture Stress Index
def calculate_smsi(soil_moisture, field_capacity=0.35, wilting_point=0.1):
    sms = (field_capacity - soil_moisture) / (field_capacity - wilting_point)
    sms = np.clip(sms, 0, 1)
    return sms

# CNN Model for Thermal Image Classification
def create_cnn(input_shape=(24, 32, 1), num_classes=3):
    model = Sequential()
    model.add(Conv2D(16, (3,3), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D((2,2)))
    model.add(Conv2D(32, (3,3), activation='relu'))
    model.add(MaxPooling2D((2,2)))
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Instantiate CNN
cnn_model = create_cnn()


# Main Loop
frame = np.zeros((24*32,))
try:
    while True:
        # Thermal camera 
        mlx.getFrame(frame)
        thermal_image = np.reshape(frame, (24, 32))
        canopy_temp = np.mean(thermal_image)

        # Other sensors 
        air_temp, rh = read_dht22()
        soil_moisture = read_tdr()

        # Stress indices 
        cwsi = calculate_cwsi(canopy_temp, air_temp, rh)
        smsi = calculate_smsi(soil_moisture)

        # CNN preprocessing
        img = thermal_image.reshape(1, 24, 32, 1)  # add batch & channel
        img = img.astype('float32') / 100  # normalize temperature roughly
        cnn_pred = cnn_model.predict(img, verbose=0)
        cnn_class = np.argmax(cnn_pred)

        # Map CNN output to stress levels
        stress_levels = ['Low', 'Medium', 'High']
        stress_label = stress_levels[cnn_class]

        print(f"CWSI: {cwsi:.2f}, SMSI: {smsi:.2f}, CNN Stress: {stress_label}")

        # Trigger irrigation
        if cwsi > 0.5 or smsi > 0.6 or cnn_class == 2:  # High stress triggers irrigation
            print("Stress detected! Opening solenoid valve...")
            GPIO.output(SOLENOID_PIN, GPIO.HIGH)
            time.sleep(10)  # irrigation duration
            GPIO.output(SOLENOID_PIN, GPIO.LOW)
            print("Irrigation completed.")

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program terminated.")
