from kmk.kmk_keyboard import KMKKeyboard
import board

keyboard = KMKKeyboard()

# griglia
keyboard.row_pins(board.GP8, board.GP9, board.GP7)
keyboard.col_pins(board.GP4, board.GP3, board.GP2, board.GP1)

# diodi
keyboard.diode_orientation = 0