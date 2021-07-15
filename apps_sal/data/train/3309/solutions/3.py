c='black brown red orange yellow green blue violet gray white'.split()
def encode_resistor_colors(ohms_string):
    t, u, *p = str(int(eval(ohms_string.replace('M','*1000k').replace('k','*1000').split()[0])))
    return '%s %s %s gold' % (c[int(t)], c[int(u)], c[len(p)])
