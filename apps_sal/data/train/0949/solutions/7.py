for test in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    m = 0
    for i in range(0, n - 1):
        m1 = 0
        j = i
        while j < n - 1:
            jd = j
            if l[jd] == l[jd + 1]:
                m1 = m1 + 1
                j = j + 1
            elif jd < n - 2 and l[jd] == l[jd + 2]:
                m1 = m1 + 1
                j = j + 2
            else:
                break
        m = max(m1, m)
    print(m)
