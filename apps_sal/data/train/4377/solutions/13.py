def solve(a, b):
    alice = sum (x > y for x,y in  zip(a,b))
    bob = sum (x < y for x,y in  zip(a,b))
    if alice > bob:
        return '%s, %s: Alice made "Kurt" proud!' % (alice, bob)
    elif bob > alice:
        return '%s, %s: Bob made "Jeff" proud!' % (alice, bob)
    else:
        return '%s, %s: that looks like a "draw"! Rock on!' % (alice, bob)

