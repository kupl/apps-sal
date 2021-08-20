def riders(S, x):
    R = []
    for (i, s) in enumerate(S):
        R += R and R[-1] + s <= 100 and [R.pop() + s] or [s]
        if i + 2 == x:
            R += 100 < s * 2 and [s] * 2 or [s * 2]
    return len(R)
