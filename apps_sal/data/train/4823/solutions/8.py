ANS = {i: v for (i, v) in enumerate(('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'))}


def wallpaper(l, w, h):
    (n, r) = divmod(2 * (l + w) / 0.52 * h * 1.15, 10)
    return ANS[l and w and h and int(n) + bool(r)]
