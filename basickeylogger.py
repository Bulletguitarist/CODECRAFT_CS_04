import keyboard
from datetime import datetime

log_file = "keystrokes_log.txt"

print("Keystroke Recorder Running (Press ESC to stop)...")

def on_key(event):
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - {event.name}\n")

keyboard.on_press(on_key)
keyboard.wait("esc")
