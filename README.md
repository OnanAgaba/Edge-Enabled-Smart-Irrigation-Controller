# Edge-Enabled-Smart-Irrigation-Controller
Solar-powered system for real-time crop water stress monitoring


# 1. Project Overview
This project implements a **real-time crop water stress detection and irrigation control system** using a Raspberry Pi 5. It integrates:

- **MLX90640 thermal camera** for canopy temperature monitoring  
- **DHT22** for ambient temperature and humidity  
- **TDR-305N** for soil moisture  
- **Solenoid valve** for irrigation control  

The system calculates the **Crop Water Stress Index (CWSI)** and **Soil Moisture Stress Index (SMSI)** to determine plant water stress. If either index exceeds user-defined thresholds, the solenoid valve automatically delivers water. This enables **edge-based, real-time smart irrigation management**.


<img width="2762" height="1812" alt="circuit_image (1)" src="https://github.com/user-attachments/assets/1b2b7723-1920-4c89-b907-6166f928d6c0" />

# 2. Components
The following are the major units of the system and their respective components.

## 2.1 Power Unit

| Component | Description | Estimated Cost (USD) |
|------------|--------------|----------------------|
| **Solar Panel (6V)** | Provides renewable energy to charge the battery and power the system. | $ — |
| **Adafruit BQ24074 Solar-DC-USB LiPo Charger** | Manages solar/USB input to safely charge the LiPo battery and power the load. | $ — |
| **LiPo Battery Pack (3S)** | Main energy storage and backup power source during low sunlight. | $ — |
| **3S 10A Li-ion 18650 Charger Protection Board (BMS Module)** | Protects and balances the 3-cell Li-ion battery pack during charging and discharging. | $ — |
| **24/12V Buck Converter** | Steps down input voltage to 5V for powering the Raspberry Pi. | $ — |
| **Adafruit MiniBoost 5V 100mA Charge Pump (AP3602A)** | Boost converter providing 5V output from a lower voltage input. | $ — |

---

## 2.2 Control Unit

| Component | Description | Estimated Cost (USD) |
|------------|--------------|----------------------|
| **Raspberry Pi 5** | Central processing and control unit; runs CNN model for edge data processing and system management. | $ — |

---

## 2.3 Sensing Unit

| Component | Description | Estimated Cost (USD) |
|------------|--------------|----------------------|
| **Adafruit MLX90640 Thermal Camera** | Captures thermal data for crop canopy temperature analysis. | $ — |
| **DHT22 Sensor** | Measures ambient temperature and humidity. | $ — |
| **TDR-305N Soil Moisture Sensor** | Measures soil volumetric water content using time-domain reflectometry. | $ — |
| **Solenoid Electrovalve (5V)** | Electrically controlled valve for irrigation management. | $ — |

---

# 4. Documented Code
## 4.1 Code Overview
The main script `crop_water_stress.py` performs the following:

a. **Sensor Initialization**  
   - Initializes MLX90640 thermal camera (I2C), DHT22, and TDR-305N sensors.
     
b. **Data Capture**  
   - Captures a 24×32 thermal image.  
   - Reads ambient temperature, humidity, and soil moisture.
     
c. **Stress Index Calculation**  
   - **CWSI**: based on canopy temp, air temp, and relative humidity.  
   - **SMSI**: based on soil moisture relative to field capacity and wilting point.
     
d. **Decision Logic**  
   - If **CWSI > 0.5** or **SMSI > 0.6**, the solenoid valve is opened for irrigation.
     
e. **Continuous Loop**
   - The system continuously monitors stress indices and updates irrigation actions in real-time.
---
## 4.2 Setup and Usage

### a. Clone the Repository
```bash
git clone https://github.com/yourusername/crop-water-stress-system.git
cd crop-water-stress-system
```
### b. Install Depenedences
```
sudo apt update
sudo apt install python3-pip
pip3 install numpy RPi.GPIO adafruit-circuitpython-mlx90640
```
### c. Connect Sensors and Actuators
Follow the wiring tables provided above. 
Ensure the MLX90640, DHT22, TDR, and solenoid valve are connected to correct GPIO/I2C pins.
### d. Run the Code
```
python3 crop_water_stress.py
```
The program prints CWSI and SMSI values to the console.
Irrigation is automatically triggered based on thresholds.

# 5. Mobile App and Web Application
An interactive web dashboard is under development and testing




