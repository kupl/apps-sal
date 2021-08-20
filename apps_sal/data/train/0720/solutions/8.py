cnt1_max = 315
arr_size = [None] * cnt1_max
for i in range(1, cnt1_max + 1):
    arr_size[i - 1] = (i * (i + 1), i)
t = int(input())
for _t in range(t):
    s = input()
    n = len(s)
    tot1 = [0] * (n + 1)
    for i in range(1, n + 1):
        if s[i - 1] == '1':
            tot1[i] = tot1[i - 1] + 1
        else:
            tot1[i] = tot1[i - 1]
    beauty = 0
    for (size, cnt) in arr_size:
        i = 0
        limit = n - size
        while i < limit + 1:
            cnt1 = tot1[i + size] - tot1[i]
            if cnt1 == cnt:
                beauty += 1
                i += 1
            else:
                i += abs(cnt1 - cnt)
    print(beauty)
