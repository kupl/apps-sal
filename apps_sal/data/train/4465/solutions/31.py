def super_size(n):
    q = []
    for i in str(n):
        q.append(i)

    q.sort(reverse=True)
    q = ''.join(q)
    return int(q)
