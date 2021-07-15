from math import log
def meters(x):
    prefixes = ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
    order = int(log(x, 1000))
    return "{:g}{}m".format(x / (1000**order or 1), prefixes[order])
