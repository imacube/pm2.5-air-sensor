# Adafruit PM2.5 Air Quality Sensor

Basic code to run this on a Raspberry Pi and record the data to a CSV file. All data is written out to the CSV file
`pm.csv` and printed to STDOUT. There is code that can be uncommented in `sense.py` for a more organized STDOUT.

# Wiring

The PM2.5 sensor uses 5V DC. 

Use the Raspberry Pi 5V and GND pins accordingly. Connect TXD on the sensor to the Raspberry Pi pin GPIO 15 (RXD).  

# Data
    
The output data has three forms: `*_standard`, `*_environment`, and `particles_*`. A Jupyter notebook has been 
included, `Filter-High-Low-Comparison.ipynb`, as an example for loading the data and examining it.

## *_standard

This data is used for manufacturer calibration and should not be used as a representation of environmental data.

## *_environment

TBD

## particiles_*

TBD

# References:
* https://learn.adafruit.com/pm25-air-quality-sensor
* https://www.adafruit.com/product/3686
