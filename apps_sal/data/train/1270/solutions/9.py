# cook your dish here
for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    queue1 = [a[0]]
    summ = a[0]
    res = -1
    for i in range(1, len(a)):
        queue2 = []
        s = set()
        summ += a[i]
        for x in queue1:
            if x not in s:
                queue2.append(x)
                s.add(x)
            if a[i] not in s:
                queue2.append(a[i])
                s.add(a[i])
            if x + a[i] not in s:
                queue2.append(x + a[i])
                s.add(x + a[i])
            if (x + a[i]) >= k and (summ - x - a[i]) >= k:
                res = i + 1
                break
            if (a[i]) >= k and (summ - a[i]) >= k:
                res = i + 1
                break
        if res != -1:
            break
        queue1 = queue2
    print(res)
