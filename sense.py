import csv
import time

try:
    import struct
except ImportError:
    import ustruct as struct

# Connect the sensor TX pin to the board/computer RX pin
# For use with a microcontroller board:
# import board
# import busio
# uart = busio.UART(board.TX, board.RX, baudrate=9600)

# For use with Raspberry Pi/Linux:
import serial


# For use with USB-to-serial cable:
# import serial
# uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=0.25)



def main(csv_writer):
    """Called when run as a script.

    :param csv_writer:
    :return:
    """

    buffer = []
    uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

    while True:
        data = uart.read(32)  # read up to 32 bytes
        data = list(data)
        # print("read: ", data)          # this is a bytearray type

        buffer += data

        while buffer and buffer[0] != 0x42:
            buffer.pop(0)

        if len(buffer) > 200:
            buffer = []  # avoid an overrun if all bad data
        if len(buffer) < 32:
            continue

        if buffer[1] != 0x4d:
            buffer.pop(0)
            continue

        frame_len = struct.unpack(">H", bytes(buffer[2:4]))[0]
        if frame_len != 28:
            buffer = []
            continue

        frame = struct.unpack(">HHHHHHHHHHHHHH", bytes(buffer[4:]))

        pm10_standard, pm25_standard, pm100_standard, pm10_env, \
        pm25_env, pm100_env, particles_03um, particles_05um, particles_10um, \
        particles_25um, particles_50um, particles_100um, skip, checksum = frame

        check = sum(buffer[0:30])

        if check != checksum:
            buffer = []
            continue

        csv_writer.writerow(frame)
        print(frame)

        # print("Concentration Units (standard)")
        # print("---------------------------------------")
        # print("PM 1.0: %d\tPM2.5: %d\tPM10: %d" %
        #       (pm10_standard, pm25_standard, pm100_standard))
        # print("Concentration Units (environmental)")
        # print("---------------------------------------")
        # print("PM 1.0: %d\tPM2.5: %d\tPM10: %d" % (pm10_env, pm25_env, pm100_env))
        # print("---------------------------------------")
        # print("Particles > 0.3um / 0.1L air:", particles_03um)
        # print("Particles > 0.5um / 0.1L air:", particles_05um)
        # print("Particles > 1.0um / 0.1L air:", particles_10um)
        # print("Particles > 2.5um / 0.1L air:", particles_25um)
        # print("Particles > 5.0um / 0.1L air:", particles_50um)
        # print("Particles > 10 um / 0.1L air:", particles_100um)
        # print("---------------------------------------")

        buffer = buffer[32:]
        # print("Buffer ", buffer)

        # Unless rapid change is happening the update interval is typically 2.3 seconds
        # https://learn.adafruit.com/pm25-air-quality-sensor/usage-notes
        time.sleep(3)


if __name__ == '__main__':
    with open('pm.csv', 'a') as csvfile:
        main(csv_writer=csv.writer(csvfile))
