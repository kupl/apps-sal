c = 'black brown red orange yellow green blue violet gray white'.split()


def encode_resistor_colors(ohms_string):
    ohms = str(int(eval(ohms_string.replace('k', '*1000').replace('M', '*1000000').split()[0])))
    return '%s %s %s gold' % (c[int(ohms[0])], c[int(ohms[1])], c[len(ohms[2:])])
