
# Wiring Details
## Power Unit Wiring

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

## Control Unit Wiring

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

## Sensing Unit Wiring

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
