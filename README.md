# Edge-Enabled-Smart-Irrigation-Controller
A low-cost open-source solar-powered system for real-time crop water stress monitoring

## 1. Project Overview
This project implements a **real-time crop water stress detection and irrigation control system** using a Raspberry Pi 5. It integrates:

- **MLX90640 thermal camera** for canopy temperature monitoring  
- **DHT22** for ambient temperature and humidity  
- **TDR-305N** for soil moisture  
- **Solenoid valve** for irrigation control  

The system calculates the **Crop Water Stress Index (CWSI)** and **Soil Moisture Stress Index (SMSI)** to determine plant water stress. If either index exceeds user-defined thresholds, the solenoid valve automatically delivers water. This enables **edge-based, real-time smart irrigation management**.


<img width="2762" height="1812" alt="circuit_image (1)" src="https://github.com/user-attachments/assets/1b2b7723-1920-4c89-b907-6166f928d6c0" />

## 2. Components
The following are the major units of the system and their respective components.
| Unit | Component | Description | Cost (USD) |
|------|-----------|-------------|------------|
| Power | Solar Panel (6V) | Charges battery & powers system | $ — |
| Power | Adafruit BQ24074 LiPo Charger | Safely charges LiPo & powers load | $ — |
| Power | LiPo Battery Pack (3S) | Backup power | $ — |
| Power | 3S 10A Li-ion BMS | Protects & balances battery | $ — |
| Power | 24/12V Buck Converter | Steps down voltage to 5V | $ — |
| Power | Adafruit MiniBoost 5V 100mA | Boost converter 5V output | $ — |
| Control | Raspberry Pi 5 | Main processor; runs CNN & controls system | $ — |
| Sensing | MLX90640 Thermal Camera | Captures canopy temperature | $ — |
| Sensing | DHT22 Sensor | Measures temperature & humidity | $ — |
| Sensing | TDR-305N Sensor | Measures soil moisture | $ — |
| Sensing | Solenoid Valve (5V) | Controls irrigation | $ — |


## 3. Documented Code

### 3.1 Code Overview
The main script `crop_water_stress.py` performs the following:

<img width="1719" height="2698" alt="irrigation" src="https://github.com/user-attachments/assets/bd256a72-6dc2-4362-9fec-9ebc78bdd014" />

---

### 3.2 Setup and Usage
**a. Clone the Repository**
```bash
git clone https://github.com/OnanAgaba/Edge-Enabled-Smart-Irrigation-Controller.git
cd Edge-Enabled-Smart-Irrigation-Controller
```
**b. Install Dependences**
```
sudo apt update
sudo apt install python3-pip
pip3 install numpy RPi.GPIO adafruit-circuitpython-mlx90640 tensorflow
```
**c. Connect Sensors and Actuators**

Follow the wiring tables provided in the `wiring.md`. 
Ensure the MLX90640, DHT22, TDR, and solenoid valve are connected to correct GPIO/I2C pins.

**d. Run the Code**
```
python3 crop_water_stress.py
```
The program prints CWSI and SMSI values to the console.
Irrigation is automatically triggered based on thresholds.

## 4. Visualization 
An interactive web dashboard and mobile app are still under development and testing 




## Contact
*For questions, contact: [Onan Agaba](mailto:onanagaba@gmail.com)*

