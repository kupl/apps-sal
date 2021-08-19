from bisect import bisect_left, insort_left
a = []
n = int(input())
for _ in range(n):
    # print(a)
    s, d = list(map(int, input().split()))
    if len(a) == 0:
        print(s, s + d - 1)
        a.append((s, s + d - 1))
        continue
    p = bisect_left(a, (s, s + d - 1))
    #print('p', p)
    ok = True
    if p > 0 and a[p - 1][1] >= s:
        ok = False
    if p < len(a) and a[p][0] <= s + d - 1:
        ok = False
    if ok:
        insort_left(a, (s, s + d - 1))
        print(s, s + d - 1)
    else:
        ok = False
        for i in range(len(a)):
            if i == 0:
                if a[0][0] > d:
                    print(1, d)
                    a = [(1, d)] + a
                    ok = True
                    break
            else:
                if a[i - 1][1] + d < a[i][0]:
                    print(a[i - 1][1] + 1, a[i - 1][1] + d)
                    insort_left(a, (a[i - 1][1] + 1, a[i - 1][1] + d))
                    ok = True
                    break
        if not ok:
            print(a[-1][1] + 1, a[-1][1] + d)
            insort_left(a, (a[-1][1] + 1, a[-1][1] + d))
