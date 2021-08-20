def solve(a, b):
    alice = sum((x > y for (x, y) in zip(a, b)))
    bob = sum((x < y for (x, y) in zip(a, b)))
    return ('{}, {}: Alice made "Kurt" proud!' if alice > bob else '{}, {}: Bob made "Jeff" proud!' if alice < bob else '{}, {}: that looks like a "draw"! Rock on!').format(alice, bob)
