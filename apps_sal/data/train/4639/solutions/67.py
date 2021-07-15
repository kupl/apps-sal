import math

power_of_two = lambda x : not (bin(x)[2:].count('1')-1) if x != 0 else False
