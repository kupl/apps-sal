import math


def wallpaper(l, w, h):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
    if l == 0 or w == 0 or h == 0:
        return numbers[0]
    return numbers[math.ceil((l + w) * h * 2.0 * 10.0 * 1.15 / 52.0)]
