def is_hollow(x):
    # Find the limits of the centre zeroes
    i = j = len(x) // 2
    while i > 0 and x[i - 1] == 0:
        i -= 1
    while j < len(x) and x[j] == 0:
        j += 1
    # Grab the 'ends'
    prefix = x[:i]
    suffix = x[j:]
    # Check conditions
    return not (j - i < 3 or 0 in prefix + suffix or len(prefix) != len(suffix))
