def convert_temp(temp, from_scale, to_scale):
    input_lookup = {'C': lambda x: x + 273.15, 'F': lambda x: (x + 359.67) * 5 / 9, 'K': lambda x: x, 'R': lambda x: x * 5 / 9, 'De': lambda x: 373.15 - x * 2 / 3, 'N': lambda x: x * 100 / 33 + 273.15, 'Re': lambda x: x * 5 / 4 + 273.15, 'Ro': lambda x: (x - 7.5) * 40 / 21 + 273.15}
    output_lookup = {'C': lambda x: x - 273.15, 'F': lambda x: x * 9 / 5 - 459.67, 'K': lambda x: x, 'R': lambda x: x * 9 / 5, 'De': lambda x: (373.15 - x) * 3 / 2, 'N': lambda x: (x - 273.15) * 33 / 100, 'Re': lambda x: (x - 273.15) * 4 / 5, 'Ro': lambda x: (x - 273.15) * 21 / 40 + 7.5}
    return round(output_lookup[to_scale](input_lookup[from_scale](temp)))
