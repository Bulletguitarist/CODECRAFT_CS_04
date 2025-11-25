# Keylogger (Educational & Safe Version) 
## Introduction

This project is an **educational, safe, and beginner‑friendly** demonstration of how a basic keylogger works. It is designed **only for learning cybersecurity concepts**, such as keyboard event capturing and understanding how attackers misuse such tools.

This version **does NOT hide itself**, **does NOT run silently**, and is meant purely for awareness and practice.

---

## What This Tool Does

* Records every key you press
* Saves all keystrokes in a text file
* Stops when you press the **ESC** key
* Helps beginners understand monitoring and event handling in Python

---

## Features

* Very simple and safe
* Logs keypresses with timestamps
* Stores output in `keystrokes_log.txt`
* Runs in the terminal, fully visible to the user

---

## File Included

* **basickeylogger.py** — Main Python script

---

## How It Works (Easy Explanation)

1. Program starts logging every key you press.
2. Each key is saved in a log file with the date and time.
3. Recording continues until you press **ESC**.
4. File `keystrokes_log.txt` stores all captured keys.

This teaches how event listeners work in Python.

---

## Python Code

```
import keyboard
from datetime import datetime

log_file = "keystrokes_log.txt"

print("Keystroke Recorder Running (Press ESC to stop)...")

def on_key(event):
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - {event.name}\n")

keyboard.on_press(on_key)
keyboard.wait("esc")
```

---

## How to Run

1. Install Python
2. Install keyboard module:

```
pip install keyboard
```

3. Save the code as **basickeylogger.py**
4. Run the script:

```
python basickeylogger.py
```

5. Press keys normally — they will be recorded
6. Press **ESC** to stop logging
7. Open `keystrokes_log.txt` to view results

---

## Example Output (Inside keystrokes_log.txt)

```
2025-02-12 10:21:45.123456 - h
2025-02-12 10:21:45.345678 - e
2025-02-12 10:21:45.567890 - l
2025-02-12 10:21:45.789012 - l
2025-02-12 10:21:46.012345 - o
```

---

## Important Note

This project is meant **only for educational cybersecurity learning**.
Never use keyloggers on someone else's device. Always take permission.

---

## Author

Jyotirmoy Mahapatra
