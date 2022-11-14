# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name': 'macOS',       # Application name
    'macros': [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'esc', [Keycode.ESCAPE]),
        (0x000000, 'tab', [Keycode.TAB]),
        (0x000000, 'delete', [Keycode.BACKSPACE]),
        # 2nd row ----------
        (0x000000, '< Back', [Keycode.COMMAND, Keycode.LEFT_ARROW]),
        (0x000000, 'Fwd >', [Keycode.COMMAND, Keycode.RIGHT_ARROW]),
        (0x000000, 'Reload', [Keycode.COMMAND, 'r']),        
        # 3rd row ----------
        (0x000000, 'Save', [Keycode.COMMAND, 's']),
        (0x000000, 'Enter', [Keycode.ENTER]),
        (0x000000, 'Cmd+d', [Keycode.COMMAND, 'd']),
        # 4th row ----------
        (0x000000, 'Close', [Keycode.COMMAND, 'w']),  # Close tab
        (0x000000, 'Reopen', [Keycode.COMMAND, Keycode.LEFT_SHIFT, 't']),  # Undo Close tab
        (0x000000, 'F12', [Keycode.F12]),  # Open Chrome/Safari/Firefox Developer tools
        # Encoder button ---
        (0x000000, '', [Keycode.OPTION, Keycode.COMMAND, Keycode.ESCAPE])  # Force Quit
    ]
}
