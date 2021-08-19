from bisect import insort_left, bisect_left
n = int(input())
s = list(input())
Q = int(input())
query = [input() for _ in range(Q)]
dic = {chr(i + ord('a')): [] for i in range(26)}
for (ind, c) in enumerate(s):
    dic[c].append(ind)
for q in query:
    (t, a, b) = q.split()
    a = int(a) - 1
    if t == '1':
        if s[a] == b:
            continue
        ind = bisect_left(dic[s[a]], a)
        dic[s[a]].pop(ind)
        insort_left(dic[b], a)
        s[a] = b
    else:
        b = int(b) - 1
        tmp = 0
        for li in list(dic.values()):
            if li and a <= li[-1] and (li[bisect_left(li, a)] <= b):
                tmp += 1
        print(tmp)
