def f1(x): return 1 if x == 'n' else 0
def f2(x): return 'Woohoo!' if x <= 15 else "Car Dead"


def bumps(road):
    # your code here
    return f2(sum((f1(x) for x in road)))
