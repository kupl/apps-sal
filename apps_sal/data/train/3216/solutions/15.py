from scipy.special import lambertw
from math import ceil, log

def movie(a, b, c):
    log_c = log(c)
    w = lambertw(
        (c ** (a / b + c / (1 - c) + 1 / b + 1) * log_c) /
        (1 - c)).real
    return int(ceil((
        b * w - b * c * w -
        a * log(c) + a * c * log_c - b * c * log_c + c * log_c - log_c
    ) / (b * (c - 1) * log_c)))
