for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    s = list(set(l))
    s.sort()
    arr = []
    for i in s:
        a = []
        for j in range(n):
            if i == l[j]:
                a.append(j)
        arr.append(a)
    if len(arr) == 1:
        print(l[0])
    else:
        count = 1
        m = 0
        c = -1
        for i in arr:
            c += 1
            for j in range(len(i) - 1):
                if j == 0:
                    p = i[j]
                if i[j + 1] - p > 1:
                    count += 1
                    p = i[j + 1]
            if m < count:
                m = count
                x = s[c]
            count = 1
        print(x)
