import math


def wallpaper(l, w, h):
    # assuming to cover the wall with wallpaper vertically roll by roll, so it's likely the roll strip will be partially used
    # number of rolls needed
    if l == 0 or w == 0 or h == 0:
        return 'zero'
    r = math.ceil((2 * (l + w) * 100) * h * 100 * 1.15 / (52 * 1000))
    number_dictionary = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty'}
    return number_dictionary[r]
