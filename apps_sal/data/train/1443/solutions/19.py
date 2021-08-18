def fact(i):
    a = i
    while a > 1:
        i += (a - 1)
        a = a - 1
    return i


for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    matrix = [0] * m
    for _ in range(n):
        s = input()
        for i in range(len(s)):
            if s[i] == '1':
                matrix[i] += 1
    coll = [fact(matrix[i] - 1) for i in range(m) if matrix[i] > 1]
    print((sum(coll) if coll else 0))
