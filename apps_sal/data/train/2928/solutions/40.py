def alphabet_war(fight):
    left = {'w': 4,
            'p': 3,
            'b': 2,
            's': 1}
    right = {'m': 4,
             'q': 3,
             'd': 2,
             'z': 1}
    total1 = 0
    total2 = 0
    for i in range(len(fight)):
        for j1 in left:
            if fight[i] == j1:
                total1 += left[j1]

        for m1 in right:
            if fight[i] == m1:
                total2 += right[m1]

    if total1 > total2:
        return "Left side wins!"
    elif total1 == total2:
        return "Let's fight again!"
    elif total1 < total2:
        return "Right side wins!"




