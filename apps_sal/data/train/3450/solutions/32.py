import numpy as np


def array(string):
    a = string.split(',')
    if len(a) <= 2:
        return None
    else:
        return ' '.join(a[1:len(a) - 1])
