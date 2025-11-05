# Edge-Enabled-Smart-Irrigation-Controller
Solar-powered system for real-time crop water stress monitoring


# Project Overview
This project implements a **real-time crop water stress detection and irrigation control system** using a Raspberry Pi 5. It integrates:

- **MLX90640 thermal camera** for canopy temperature monitoring  
- **DHT22** for ambient temperature and humidity  
- **TDR-305N** for soil moisture  
- **Solenoid valve** for irrigation control  

The system calculates the **Crop Water Stress Index (CWSI)** and **Soil Moisture Stress Index (SMSI)** to determine plant water stress. If either index exceeds user-defined thresholds, the solenoid valve automatically delivers water. This enables **edge-based, real-time smart irrigation management**.


<img width="2762" height="1812" alt="circuit_image (1)" src="https://github.com/user-attachments/assets/1b2b7723-1920-4c89-b907-6166f928d6c0" />

# Components
The following are the major units of the systems and their respective components
1. Power Unit

| Component | Description | Pins | Estimated Cost (USD) |
|------------|--------------|------|----------------------|
| **Solar Panel (6V)** | Provides renewable energy to charge the battery and power the system. | +, - | $ — |
| **Adafruit BQ24074 Solar-DC-USB LiPo Charger** | Manages solar/USB input to safely charge the LiPo battery and power the load. | D+, D-, GND, VLIPO, OUT, !CHG, !PGOOD, !CE, ISET, THERM, VBUS | $ — |
| **LiPo Battery Pack (3S)** | Main energy storage and backup power source during low sunlight. | +, - | $ — |
| **3S 10A Li-ion 18650 Charger Protection Board (BMS Module)** | Protects and balances the 3-cell Li-ion battery pack during charging and discharging. | B+, B2, B1, P-, P+, B- | $ — |
| **24/12V Buck Converter** | Steps down input voltage to 5V for powering the Raspberry Pi. | VIN+, VIN-, 5V, GND | $ — |
| **Adafruit MiniBoost 5V 100mA Charge Pump (AP3602A)** | Boost converter providing 5V output from a lower voltage input. | !SHDN, 5.0V, GND, VIN | $ — |

---

2. Control Unit

| Component | Description | Pins | Estimated Cost (USD) |
|------------|--------------|------|----------------------|
| **Raspberry Pi 5** | Central processing and control unit; runs CNN model for edge data processing and system management. | Type-C, Micro HDMI 1 & 2, Camera 1 & 2, PoE, Fan, PCIe, USB 3.0/2.0, Ethernet, 5V, GND, 3.3V, multiple GPIOs | $ — |

---

3.  Sensing Unit

| Component | Description | Pins | Estimated Cost (USD) |
|------------|--------------|------|----------------------|
| **Adafruit MLX90640 Thermal Camera** | Captures thermal data for crop canopy temperature analysis. | VCC, 3.3V, GND, SCL, SDA | $ — |
| **DHT22 Sensor** | Measures ambient temperature and humidity. | GND, VCC, DAT | $ — |
| **TDR-305N Soil Moisture Sensor** | Measures soil volumetric water content using time-domain reflectometry. | Pin 1, Pin 2, Pin 3 | $ — |
| **Solenoid Electrovalve (5V)** | Electrically controlled valve for irrigation management. | VCC, GND | $ — |

---

# Wiring Details
1. Power Unit Wiring

| Component | Pin | Connected To |
|------------|-----|--------------|
| **Solar Panel** | + | D+ on Adafruit BQ24074 Solar-DC-USB LiPo Charger |
|  | - | D- on Adafruit BQ24074 Solar-DC-USB LiPo Charger |
| **Adafruit BQ24074 Solar-DC-USB LiPo Charger** | D+ | + on Solar Panel |
|  | D- | - on Solar Panel |
|  | GND | B1 on 3S 10A Li-ion Charger Protection Board, GND on Adafruit MiniBoost |
|  | VLIPO | VIN on Adafruit MiniBoost, B+ on 3S 10A Charger Protection Board |
| **3S 10A Li-ion Charger Protection Board** | B+ | VLIPO on Adafruit BQ24074, VIN on MiniBoost |
|  | B1 | GND on Adafruit BQ24074, GND on MiniBoost |
|  | P+ | VIN+ on 24/12V Buck Converter |
|  | P- | VIN- on 24/12V Buck Converter |
| **Battery (3S LiPo)** | + | B+ on 3S Charger Protection Board |
|  | - | B1 on 3S Charger Protection Board |
| **Adafruit MiniBoost 5V 100mA Charge Pump (AP3602A)** | VIN | B+ on 3S Charger Board, VLIPO on Adafruit BQ24074 |
|  | GND | GND on Adafruit BQ24074 and B1 on 3S Charger Board |
|  | 5.0V | Pin 1 on TDR |
| **24/12V Buck Converter** | VIN+ | P+ on 3S Charger Board, OUT on Adafruit BQ24074 |
|  | VIN- | P- on 3S Charger Board, GND on Adafruit BQ24074 |
|  | 5V | 5V on Raspberry Pi |
|  | GND | GND on Raspberry Pi |

---

2. Control Unit Wiring

| Component | Pin | Connected To |
|------------|-----|--------------|
| **Raspberry Pi 5** | 5V | 5V on Buck Converter, VCC on Solenoid Electrovalve |
|  | GND | GND on Buck Converter, GND on MLX90640, GND on DHT22, GND on Solenoid Electrovalve, Pin 3 on TDR |
|  | 3.3V | VCC on MLX90640 and VCC on DHT22 |
|  | GPIO 2 | SDA on MLX90640 |
|  | GPIO 3 | SCL on MLX90640 |
|  | GPIO 5 | DAT on DHT22 |
|  | GPIO 6 | Pin 2 on TDR |
| **Solenoid Electrovalve** | VCC | 5V on Raspberry Pi |
|  | GND | GND on Raspberry Pi and GND on DHT22 |

---

3. Sensing Unit Wiring

| Sensor | Pin | Connected To |
|---------|-----|--------------|
| **Adafruit MLX90640 Thermal Camera** | VCC | 3.3V on Raspberry Pi |
|  | GND | GND on Raspberry Pi |
|  | SCL | GPIO 3 on Raspberry Pi |
|  | SDA | GPIO 2 on Raspberry Pi |
| **DHT22** | VCC | 3.3V on Raspberry Pi |
|  | GND | GND on Raspberry Pi and GND on Solenoid Electrovalve |
|  | DAT | GPIO 5 on Raspberry Pi |
| **TDR-305N** | Pin 1 | 5.0V on Adafruit MiniBoost |
|  | Pin 2 | GPIO 6 on Raspberry Pi |
|  | Pin 3 | GND on Raspberry Pi |

# Documented Code
The system captures real-time data from an MLX90640 thermal camera, a DHT22 temperature and humidity sensor, and a TDR-305N soil moisture sensor on a Raspberry Pi 5. It calculates the Crop Water Stress Index (CWSI) from canopy and air temperature and relative humidity, and the Soil Moisture Stress Index (SMSI) from soil moisture relative to field capacity and wilting point. If either index exceeds predefined thresholds, the solenoid valve is automatically activated to irrigate the crop, delivering water for a specified duration. The process repeats continuously, enabling real-time monitoring and edge-based irrigation control for optimal crop water management.

# Mobile App and Web Application
Under development and testing



## 🖥️ Code Overview

The main script `crop_water_stress.py` performs the following:

1. **Sensor Initialization**  
   - Initializes MLX90640 thermal camera (I2C), DHT22, and TDR-305N sensors.  
2. **Data Capture**  
   - Captures a 24×32 thermal image.  
   - Reads ambient temperature, humidity, and soil moisture.  
3. **Stress Index Calculation**  
   - **CWSI**: based on canopy temp, air temp, and relative humidity.  
   - **SMSI**: based on soil moisture relative to field capacity and wilting point.  
4. **Decision Logic**  
   - If **CWSI > 0.5** or **SMSI > 0.6**, the solenoid valve is opened for irrigation.  
5. **Continuous Loop**  
   - The system continuously monitors stress indices and updates irrigation actions in real-time.

---

## ⚙️ Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/crop-water-stress-system.git
cd crop-water-stress-system
```

### 2. Install Depenedences
```
sudo apt update
sudo apt install python3-pip
pip3 install numpy RPi.GPIO adafruit-circuitpython-mlx90640
```

### 3. Connect Sensors and Actuators
Follow the wiring tables provided above. 
Ensure the MLX90640, DHT22, TDR, and solenoid valve are connected to correct GPIO/I2C pins.

### 4. Run the Code
```
python3 crop_water_stress.py
```
The program prints CWSI and SMSI values to the console.
Irrigation is automatically triggered based on thresholds.

