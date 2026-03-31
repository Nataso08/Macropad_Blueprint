from kmk.keys import KC
from kb import keyboard

keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D],   # Layer 0
    [KC.F, KC.G, KC.H, KC.I]    # Layer 1
    [KC.L, KC.M, KC.N, KC.O]    # Layer 1
]

if __name__ == "__main__":
    keyboard.go()