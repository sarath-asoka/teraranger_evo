import smbus2  # This library provides I2C support for Python 3
import time

# Define the I2C address of the TeraRanger Evo
DEVICE_ADDRESS = 0x31

# Define the command for getting the distance reading
COMMAND_GET_DISTANCE = 0x00

# Define the number of bytes to read back from the TeraRanger Evo (3 bytes for distance reading)
BYTES_TO_READ = 3

# Open a connection to the I2C bus
bus = smbus2.SMBus(1)  # Change this number to match the I2C bus you're using (e.g. 0 for Raspberry Pi 1)

# Send the command to get the distance reading
bus.write_byte(DEVICE_ADDRESS, COMMAND_GET_DISTANCE)

# Wait for the sensor to respond (50ms is enough for the TeraRanger Evo)
time.sleep(0.05)

# Read the distance data from the sensor
distance_data = bus.read_i2c_block_data(DEVICE_ADDRESS, 0, BYTES_TO_READ)

# Convert the distance data to a distance value in millimeters
distance = distance_data[0] << 8 | distance_data[1]
# The third byte is a checksum and can be ignored

print("Distance: {} mm".format(distance))
