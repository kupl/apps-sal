def squares_needed(g):
    y = 0
    z = 0
    for x in range(64):
        if x == 0 and g == 0:
            return (x)
            break
        elif x >= 1:
            if g / 2 ** x < 2 and g / 2 ** x > 1:
                y = g / 2 ** x
                return (x + 1)
                break
            elif g / 2 ** x <= 0.5:
                return (x)
                break


y = squares_needed(562949953421312)
print(y)
