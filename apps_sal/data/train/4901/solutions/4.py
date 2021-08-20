from fractions import gcd


def calculate_ratio(w, h):
    c = gcd(w, h)
    return '{}:{}'.format(w / c, h / c) if w > 0 and h > 0 else 'You threw an error'
