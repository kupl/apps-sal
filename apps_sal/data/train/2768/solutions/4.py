def solve(n):
    (li, r) = (list(range(2, n + 1)), [1])
    while 1:
        r.append(li[0])
        if li[0] > len(li):
            return sum(r + li[1:])
        li = [li[j] for j in range(1, len(li)) if j % li[0] != 0]
