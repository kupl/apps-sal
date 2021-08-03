for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    first = 0
    last = n - 1
    sseq = []
    while(first < last):
        if a[last] > 0:
            while(first < last):
                if a[first] < 0:
                    p = a[first]
                    q = a[last]
                    a[first] = q
                    a[last] = p
                    sseq.append(first + 1)
                    sseq.append(last + 1)
                    first += 1
                    break
                first += 1
        last -= 1
    sseq.sort()
    summ = 0
    for i in range(n):
        if a[i] >= 0:
            summ += a[i]
        else:
            break
    print(summ)
    print(len(sseq), *sseq)
