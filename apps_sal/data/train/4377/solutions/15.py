def solve(a, b):
    a_count = 0
    b_count = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            a_count += 1
        elif a[i] < b[i]:
            b_count += 1
    if a_count > b_count:
        return '{a_count}, {b_count}: Alice made "Kurt" proud!'.format(a_count=a_count, b_count=b_count)
    elif b_count > a_count:
        return '{a_count}, {b_count}: Bob made "Jeff" proud!'.format(a_count=a_count, b_count=b_count)
    else:
        return '{a_count}, {b_count}: that looks like a "draw"! Rock on!'.format(a_count=a_count, b_count=b_count)
