from scipy.ndimage.measurements import center_of_mass
from math import floor, ceil
from numpy import array


def will_it_balance(stick, terrain):
    center = center_of_mass(array(stick))[0]
    return terrain[floor(center)] and terrain[ceil(center)]
