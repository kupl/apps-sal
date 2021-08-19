for _ in range(eval(input())):
    (n, k, m) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [i - j for (i, j) in zip(a, b)]
    d = list(map(int, input().split())) + list(map(int, input().split()))
    c.sort(reverse=True)
    d.sort(reverse=True)
    j = 0
    for i in range(len(d)):
        if j >= n:
            break
        if c[j] >= d[i]:
            c[j] -= d[i]
            j += 1
    print(sum(c))
