import re
from math import log10
def encode_resistor_colors(ohms_string):
    codes = {'0': 'black', '1': 'brown', '2': 'red', '3': 'orange', '4': 'yellow',
         '5': 'green', '6': 'blue', '7': 'violet','8': 'gray','9': 'white'}

    initial_number, group = re.findall(r'([0-9.]+)([k,M])?', ohms_string).pop()
    num = float(initial_number) * int(group=='k' and 1000 or group=='M' and 1000000 or 1)
    processed_number = str(float(initial_number)*10)[:2]
    final = [codes[x] for x in processed_number] + [codes[str(int(log10(num / float(processed_number))))], 'gold']
    return ' '.join(final)
