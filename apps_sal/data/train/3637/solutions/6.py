def num_primorial(n):
    l = [2]
    k = 3
    while len(l) < n:
        l.append(k)
        for i in range(2, k):
            if k % i == 0:
                l.pop()
                break
        k += 1
    out = 1
    for i in l:
        out *= i
    return out
