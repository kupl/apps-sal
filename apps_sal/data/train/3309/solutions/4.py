import math
import re

COLORS = {'0': 'black', '1': 'brown', '2': 'red', '3': 'orange', '4': 'yellow',
          '5': 'green', '6': 'blue', '7': 'violet', '8': 'gray', '9': 'white'}

def encode_resistor_colors(ohms_string):
    ohms = re.sub(r'([0-9\.]+)([kM])?(.*)', 
                 lambda x: str(float(x[1]) * (int(x[2].translate(str.maketrans(
                 {'k': '1000', 'M': '1000000'}))) if x[2] else 1)), ohms_string)            
    return f"{' '.join(COLORS.get(x) for x in ohms[:2])} {COLORS.get(str(len(ohms[2:]) - 2))} gold"
