def f(a, n):
    (l, r, s1, s2) = ([0] * n, [0] * n, [], [])
    for i in range(n):
        count = 1
        while len(s1) > 0 and a[i] < s1[-1][0]:
            count += s1[-1][1]
            s1.pop()
        s1.append((a[i], count))
        l[i] = count
    for i in range(n - 1, -1, -1):
        count = 1
        while len(s2) > 0 and a[i] <= s2[-1][0]:
            count += s2[-1][1]
            s2.pop()
        s2.append((a[i], count))
        r[i] = count
    count = 0
    for i in range(n):
        count += a[i] * l[i] * r[i]
    return count


t = int(input())
