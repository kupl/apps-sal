def group_by_commas(n):
    n = [i for i in str(n)]
    for i in range(len(n) -4, -1, -3):
        n.insert(i+1, ',')
    return ''.join(n)

