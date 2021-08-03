import numpy as np


def validate(cc_number):
    # split integer into array of digits
    arr = np.array([int(i) for i in str(cc_number)])
    # double every second digit from the right
    arr[-2::-2] *= 2
    # substract 9 from digits greater than 9
    arr[arr > 9] -= 9
    # sum up all the digits and check the modulus 10
    return np.sum(arr) % 10 == 0
