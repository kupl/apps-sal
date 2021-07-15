def solve(a, b):
    sa = sum(1 for x, y in zip(a,b) if x > y)
    sb = sum(1 for x, y in zip(a,b) if y > x)
    return '{}, {}: {}'.format(sa, sb, 'that looks like a "draw"! Rock on!' if sa == sb else ['Bob made "Jeff" proud!', 'Alice made "Kurt" proud!'][sa > sb] )
