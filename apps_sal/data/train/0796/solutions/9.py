for t in range(int(input())):
    l = []
    n = int(input())
    for x in input().split():
        l.append(int(x))
    i = 0
    res = [0] * n
    while i < n:
        j = i + 1
        while j < n:
            if l[j - 1] * l[j] > 0:
                break
            j += 1
        curr = j - i
        for k in range(i, j):
            res[k] = curr
            curr -= 1
        i = j
    for num in res:
        print(num, end=' ')
    print()
