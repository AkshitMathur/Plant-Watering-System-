import pyfirmata
import time
import matplotlib.pyplot as plt

# Specify the COM port (e.g., "COM3" on Windows or "/dev/ttyUSB0" on Linux)
board = pyfirmata.Arduino('COM3')

# Start an iterator to avoid buffer overflow
it = pyfirmata.util.Iterator(board)
it.start()

# Define the analog pin (A0)
moisture_pin = board.get_pin('a:0:i')

# Real-time plotting setup
plt.ion()
fig, ax = plt.subplots()
x_data, y_data = [], []

while True:
    moisture_level = moisture_pin.read()
    if moisture_level is not None:
        # Convert to 0-1023 range (assuming 10-bit ADC)
        raw_value = int(moisture_level * 1023)
        
        # Convert to percentage (0% = dry, 100% = fully wet)
        moisture_percentage = (1023 - raw_value) / 1023 * 100
        print(f"Moisture Level: {moisture_percentage:.2f}%")

        # Plotting
        x_data.append(time.time())
        y_data.append(moisture_percentage)
        ax.clear()
        ax.plot(x_data, y_data, label="Moisture Level (%)")
        plt.xlabel("Time (s)")
        plt.ylabel("Moisture Level (%)")
        plt.title("Real-Time Moisture Level")
        plt.ylim(0, 100)  # Limit y-axis to 0-100%
        plt.legend()
        plt.pause(0.01)

        # Control the pump based on moisture percentage
        if moisture_percentage < 30:  # Adjust threshold as needed
            board.digital[8].write(1)  # Turn on pump
        else:
            board.digital[8].write(0)  # Turn off pump
        
    time.sleep(0.1)
