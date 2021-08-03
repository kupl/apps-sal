from collections import Counter


def cannons_ready(gunners):
    return ["Fire!", "Shiver me timbers!"][len(Counter(list(gunners.values()))) != 1]
