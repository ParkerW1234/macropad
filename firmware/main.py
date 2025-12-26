import time
import board
import busio
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import adafruit_ssd1306

KEY_PINS = (board.D0, board.D1, board.D2, board.D3, board.D6)
LAYER_KEY_INDEX = 4
OLED_W, OLED_H = 128, 32
OLED_ADDR = 0x3C
NUM_LAYERS = 3

LAYERS = [
    [
        ("Cmd+Shift+P", (Keycode.COMMAND, Keycode.SHIFT, Keycode.P)),
        ("Cmd+P",       (Keycode.COMMAND, Keycode.P)),
        ("Cmd+S",       (Keycode.COMMAND, Keycode.S)),
        ("Cmd+/",       (Keycode.COMMAND, Keycode.FORWARD_SLASH)),
    ],
    [
        ("Cmd+F",       (Keycode.COMMAND, Keycode.F)),
        ("Cmd+Shift+F", (Keycode.COMMAND, Keycode.SHIFT, Keycode.F)),
        ("Cmd+Z",       (Keycode.COMMAND, Keycode.Z)),
        ("Cmd+Y",       (Keycode.COMMAND, Keycode.Y)),
    ],
    [
        ("Cmd+Tab",     (Keycode.COMMAND, Keycode.TAB)),
        ("Cmd+W",       (Keycode.COMMAND, Keycode.W)),
        ("Cmd+T",       (Keycode.COMMAND, Keycode.T)),
        ("Cmd+R",       (Keycode.COMMAND, Keycode.R)),
    ],
]

kbd = Keyboard(usb_hid.devices)

keys = keypad.Keys(
    KEY_PINS,
    value_when_pressed=False,
    pull=True
)

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(OLED_W, OLED_H, i2c, addr=OLED_ADDR)

current_layer = 0
last_action_label = ""

def oled_show(layer_idx, last_action=""):
    oled.fill(0)
    oled.text("Hackpad", 0, 0, 1)
    oled.text(f"Layer: {layer_idx+1}/{NUM_LAYERS}", 0, 12, 1)
    if last_action:
        oled.text(last_action[:16], 0, 24, 1)
    oled.show()

def send_combo(combo):
    kbd.press(*combo)
    kbd.release_all()

oled_show(current_layer)

while True:
    event = keys.events.get()
    if event and event.pressed:
        idx = event.key_number
        if idx == LAYER_KEY_INDEX:
            current_layer = (current_layer + 1) % NUM_LAYERS
            oled_show(current_layer, "Layer changed")
        else:
            label, combo = LAYERS[current_layer][idx]
            send_combo(combo)
            oled_show(current_layer, label)
    time.sleep(0.002)
