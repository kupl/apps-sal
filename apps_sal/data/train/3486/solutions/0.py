def find_last(n, m):
    (li, start) = ([[0, i + 1] for i in range(n)], 0)
    while len(li) != 1:
        (prev, l_) = (li[start][1], len(li))
        for k in range(m):
            li[start][0] += 1
            start = (start + 1) % l_
        if m < len(li):
            k = start
            while li[k][1] != prev:
                li[k][0] += 2
                k = (k + 1) % l_
        li[start][0] += li.pop((start - 1) % l_)[0]
        start = [(start - 1) % l_, start][start == 0]
    return tuple(li[0][::-1])
