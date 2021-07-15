def solve(a, b):
    alice = sum(i > j for i, j in zip(a, b))
    bob = sum(j > i for i, j in zip(a, b))
    
    if alice == bob:
        words = 'that looks like a "draw"! Rock on!'
    elif alice > bob:
        words = 'Alice made "Kurt" proud!'
    else:
        words = 'Bob made "Jeff" proud!'
    
    return '{}, {}: {}'.format(alice, bob, words) 
