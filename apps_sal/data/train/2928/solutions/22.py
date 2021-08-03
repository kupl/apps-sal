def alphabet_war(fight):
    a = {'w': 4, 'p': 3, 'b': 2, 's': 1,
         'm': -4, 'q': -3, 'd': -2, 'z': -1}
    b = sum(a[c] for c in fight if c in a)

    return {b == 0: "Let's fight again!",
            b > 0: "Left side wins!",
            b < 0: "Right side wins!"
            }[True]
