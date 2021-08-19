import bisect
from collections import defaultdict
N = int(input())
S = list(input())
Q = int(input())
alpha_dic = defaultdict(list)
for (i, s) in enumerate(S):
    alpha_dic[s].append(i)
for _ in range(Q):
    (l, m, n) = input().split()
    if l == '1':
        m = int(m) - 1
        c = S[m]
        if c == n:
            continue
        else:
            i = bisect.bisect_left(alpha_dic[c], m)
            del alpha_dic[c][i]
            bisect.insort_left(alpha_dic[n], m)
            S[m] = n
    else:
        (m, n) = (int(m) - 1, int(n) - 1)
        cnt = 0
        for (_, val) in list(alpha_dic.items()):
            if not val:
                continue
            left_idx = bisect.bisect_left(val, m)
            right_idx = bisect.bisect_left(val, n)
            l = len(val)
            if left_idx > right_idx or (left_idx == right_idx and left_idx == l) or (left_idx == right_idx and val[left_idx] != m and (val[right_idx] != n)):
                continue
            cnt += 1
        print(cnt)
