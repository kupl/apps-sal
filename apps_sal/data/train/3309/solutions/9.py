colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'gray', 'white', 'gold']


def encode_resistor_colors(ohms_string):
    ohms = int(eval(ohms_string.split()[0].replace('k', '*1E3').replace('M', '*1E6')))
    return ' '.join((colors[i] for i in [int(str(ohms)[0]), int(str(ohms)[1]), len(str(ohms)) - 2, 10]))
