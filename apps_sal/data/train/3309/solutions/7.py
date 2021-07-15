import re
import math

REGEX_NUMBERS = r"\d+\.?\d*"
RESISTOR_COLORS = {0: 'black', 1: 'brown', 2: 'red', 3: 'orange', 4: 'yellow', 5: 'green', 6: 'blue', 7: 'violet', 8: 'gray', 9: 'white'}
MULTIPLIER = {'k': 1000, 'M': 1000000}

def encode_resistor_colors(ohms_string):
    retrieved_val = re.findall(REGEX_NUMBERS, ohms_string.replace('ohms', ''))[0]
    needs_trailing_zero = len(retrieved_val) == 1
    retrieved_val = retrieved_val + '0' if needs_trailing_zero else retrieved_val
    translation = ' '.join([RESISTOR_COLORS[int(digit)] for digit in retrieved_val if digit.isnumeric()][:2])
    for key in MULTIPLIER:
        retrieved_val = float(retrieved_val) * MULTIPLIER.get(key) if key in ohms_string else float(retrieved_val)
    subtract = 2 if needs_trailing_zero else 1
    return translation + ' '+(RESISTOR_COLORS[math.floor(math.log10(retrieved_val)) - subtract]) + ' gold'
