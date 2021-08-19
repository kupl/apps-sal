def solve(a, b):
    al = 0
    bo = 0
    for i in range(0, len(a)):
        if a[i] > b[i]:
            al += 1
        elif a[i] < b[i]:
            bo += 1
    if al > bo:
        return '{0}, {1}: Alice made "Kurt" proud!'.format(al, bo)
    elif al < bo:
        return '{0}, {1}: Bob made "Jeff" proud!'.format(al, bo)
    else:
        return '{0}, {1}: that looks like a "draw"! Rock on!'.format(al, bo)
