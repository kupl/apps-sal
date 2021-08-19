from bisect import insort_left, bisect_left
N = int(input())
S = list(input())
Q = int(input())
Query = [input() for _ in range(Q)]
dic = {chr(i + ord('a')): [] for i in range(26)}
for (i, s) in enumerate(S):
    dic[s].append(i)
for q in Query:
    (t, a, b) = q.split()
    a = int(a) - 1
    if t == '1':
        if S[a] == b:
            continue
        tmp_index = bisect_left(dic[S[a]], a)
        dic[S[a]].pop(tmp_index)
        insort_left(dic[b], a)
        S[a] = b
    elif t == '2':
        b = int(b) - 1
        cnt = 0
        for li in dic.values():
            if li and a <= li[-1] and (li[bisect_left(li, a)] <= b):
                cnt += 1
        print(cnt)
