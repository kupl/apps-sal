import re
colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'gray', 'white']


def encode_resistor_colors(ohms_string):
    split_string = ohms_string.split()
    number = split_string[0]
    if number[-1] == 'k':
        number = str(int(float(number[0:-1]) * 1000))
    elif number[-1] == 'M':
        number = str(int(float(number[0:-1]) * 1000000))
    color1 = colors[int(number[0])]
    color2 = colors[int(number[1])]
    color3 = colors[len(number) - 2]
    return color1 + ' ' + color2 + ' ' + color3 + ' gold'
