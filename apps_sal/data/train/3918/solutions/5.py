def baby_count(x):
    b = 0
    a = 0
    y = 0
    for c in x.upper():
        if c == "B":
            b += 1
        elif c == "A":
            a += 1
        elif c == "Y":
            y += 1

    count = min(a, b // 2, y)
    return count if count > 0 else 'Where\'s the baby?!'
