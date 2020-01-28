# Adafruit PM2.5 Air Quality Sensor

Basic code to run this on a Raspberry Pi and record the data to a CSV file. All data is written out to the CSV file
`pm.csv` and printed to STDOUT. There is code that can be uncommented in `sense.py` for a more organized STDOUT.

# Wiring

The PM2.5 sensor uses 5V DC. 

Use the Raspberry Pi 5V and GND pins accordingly. Connect TXD on the sensor to the Raspberry Pi pin GPIO 15 (RXD). These
three pins are all in the same row. Verify that the Pi board being used has this format before connecting anything:

**5V**, 5V, **Gnd**, GPIO 14 (TXD), **GPIO 15 (RXD)**

So starting with the first 5V pin, just connect to every other pin. But again, *verify the pins on your Raspberry Pi!* 

# Data
    
The output data has three forms: `*_standard`, `*_environment`, and `particles_*`. A Jupyter notebook has been 
included, `Filter-High-Low-Comparison.ipynb`, as an example for loading the data and examining it.

## *_standard

This data is used for manufacturer calibration and should not be used as a representation of environmental data.

## *_environment

Environmental readings.

## particles_*

Ambient readings.

# References:
* [Adafruit Learning page](https://learn.adafruit.com/pm25-air-quality-sensor)
* [Adafruit Usage Notes for device, useful details on data output](https://learn.adafruit.com/pm25-air-quality-sensor/usage-notes)
* [Adafruit Product Page](https://www.adafruit.com/product/3686)
* [Adafruit Forum about PM2.5 Units](https://forums.adafruit.com/viewtopic.php?f=19&t=135496)
* [Forum post that was used for Usage Notes above](https://forums.adafruit.com/viewtopic.php?f=48&t=136528&p=767725#p767725)
