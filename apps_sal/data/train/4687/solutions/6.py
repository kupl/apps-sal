# What a f****** mess this was...

import math
import numpy as np


def decomp(n):

    def rt(x):
        if x % 2 == 0:
            return [2, int(x / 2)]
        for i in range(3, math.floor(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return [i, int(x / i)]
        return [x, 1]

    leftovers = np.arange(2, n + 1, 1)
    facs = [0] * (n - 1)

    while leftovers != []:
        newlefts = []

        for l in leftovers:
            [h, k] = rt(l)
            facs[h - 2] += 1

            if k != 1:
                newlefts += [k]

        leftovers = newlefts

    string = ''

    for m in range(2, n + 1):
        if facs[m - 2] == 1:
            if string != '':
                string += ' * ' + str(m)
            if string == '':
                string = str(m)
        if facs[m - 2] > 1:
            if string != '':
                string += ' * ' + str(m) + '^' + str(facs[m - 2])
            if string == '':
                string = str(m) + '^' + str(facs[m - 2])

    return string
