def count_repeats(str):
    return sum((a == b for (a, b) in zip(str, str[1:])))
