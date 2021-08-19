def solve(arr):
    c = []
    answer = []
    for n in range(0, max(arr) + 1):
        c.append(arr.count(n))
    x = sorted(c, reverse=True)
    for i in x:
        m = i
        while m > 0:
            answer.append(c.index(i))
            m -= 1
        c[c.index(i)] = -1
    return answer
