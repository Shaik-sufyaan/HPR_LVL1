import serial
import time

SERIAL_PORT = 'COM3'
BAUD_RATE = 9600
LOG_FILE = 'data.txt'

def readload_cell_data():
    """Read weight from the load cell via serial."""
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
        time.sleep(2)  # Allow time for the serial connection to establish
        while True:
            # Read line from serial
            line = ser.readline().decode('utf-8').strip()
            if line:
                try:
                    weight = float(line)  # Convert to float
                    return weight
                except ValueError:
                    print("Invalid data received")

def log_data(weight):
    """Log weight data to a text file."""
    with open(LOG_FILE, 'a') as file:
        file.write(f"{weight:.2f}\n")  # Write the weight in kg with 2 decimal places

def main():
    print("Starting Load Cell Data Logging...")
    while True:
        weight = readload_cell_data()  # Read weight
        print(f"Weight: {weight:.2f} kg")  # Print to console
        log_data(weight)  # Log the weight data
        time.sleep(0.1)  # Adjust this delay for the desired reading frequency

if __name__ == "__main__":
    main()
