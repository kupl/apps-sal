def longest(s1, s2):
    x = ''
    y = sorted(s1 + s2)

    for i in y:
        if i not in x:
            x += i

    return x  # your code
