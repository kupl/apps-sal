def diffs(a, b):
    return sum(1 for aa, bb in zip(a, b) if aa != bb)

def child(bird1, bird2):
    return diffs(bird1, bird2) in [1, 2] 

def grandchild(bird1, bird2):
    l = len(bird1)
    d = diffs(bird1, bird2)
    return (d < 5 and l > 1) or (d == 0 and l == 1)

