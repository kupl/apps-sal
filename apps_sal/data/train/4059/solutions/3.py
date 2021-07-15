from itertools import accumulate, chain
from operator import xor

def switch_lights(a):
    return list(accumulate(chain([0], reversed(a)), xor))[-2::-1]
