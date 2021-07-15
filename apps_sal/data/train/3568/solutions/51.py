f1 = lambda x: 1 if x == 'n' else 0
f2 = lambda x: 'Woohoo!' if x <= 15 else "Car Dead"

def bumps(road):
    # your code here
    return f2(sum((f1(x) for x in road)))
