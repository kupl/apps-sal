def is_hollow(x):
    i = j = len(x) // 2
    while i > 0 and x[i - 1] == 0:
        i -= 1
    while j < len(x) and x[j] == 0:
        j += 1
    prefix = x[:i]
    suffix = x[j:]
    return not (j - i < 3 or 0 in prefix + suffix or len(prefix) != len(suffix))
