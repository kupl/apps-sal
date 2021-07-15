def solve(a, b):
    A = sum (x > y for x,y in  zip(a,b))
    B = sum (x < y for x,y in  zip(a,b))
    return '{}, {}: '.format(str(A),str(B)) + \
    ('that looks like a "draw"! Rock on!' if A == B else \
    ['Alice made "Kurt" proud!','Bob made "Jeff" proud!'][ A < B]) 
    # copied this last bit from daddepledge's solution. Neat!

