# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name': 'Windows Task View',       # Application name
    'macros': [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'esc', [Keycode.ESCAPE]),
        (0x000000, 'tab', [Keycode.TAB]),
        (0x000000, 'delete', [Keycode.BACKSPACE]),
        # 2nd row ----------
        (0x000000, 'W+D', [Keycode.WINDOWS, Keycode.D]),
        (0x000000, 'W+Tab',  [Keycode.WINDOWS, Keycode.TAB]),  # Windows + Tab
        (0x000000, '^W+D', [Keycode.CONTROL, Keycode.WINDOWS, Keycode.D]),        
        # 3rd row ----------
        (0x000000, '^W+<',  [Keycode.CONTROL, Keycode.WINDOWS, Keycode.LEFT_ARROW]),  # Control + Windows + ←
        (0x000000, 'W+↑',  [Keycode.WINDOWS, Keycode.UP_ARROW]),  # Windows + ↑
        (0x000000, '^W+>',  [Keycode.CONTROL, Keycode.WINDOWS, Keycode.RIGHT_ARROW]),  # Control + Windows + →
        # 4th row ----------
        (0x000000, 'W+<',  [Keycode.WINDOWS, Keycode.LEFT_ARROW]),  # Windows + ←
        (0x000000, 'W+Dn',  [Keycode.WINDOWS, Keycode.DOWN_ARROW]),  # Windows + ↓
        (0x000000, 'W+>', [Keycode.WINDOWS, Keycode.DOWN_ARROW]),  # Windows + →
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, Keycode.ALT, Keycode.DELETE])  # Force Quit
    ]
}
