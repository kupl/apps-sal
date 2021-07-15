from itertools import permutations


def late_clock(digits):
    for combo in permutations(sorted(digits, reverse=True)):
        if combo[:2] < (2, 4) and combo[2] < 6:
            return "{}{}:{}{}".format(*combo)
