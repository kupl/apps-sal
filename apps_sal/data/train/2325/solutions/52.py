from itertools import accumulate
s = input()
t = input()
q = int(input())
abcd = [tuple(map(int, input().split())) for i in range(q)]
s_number = [2 if ab == 'B' else 1 for ab in s]
t_number = [2 if ab == 'B' else 1 for ab in t]
s_sum = [0] + s_number
s_sum = list(accumulate(s_sum))
t_sum = [0] + t_number
t_sum = list(accumulate(t_sum))
for (a, b, c, d) in abcd:
    s_i = s_sum[b] - s_sum[a - 1]
    t_i = t_sum[d] - t_sum[c - 1]
    if s_i % 3 == t_i % 3:
        print('YES')
    else:
        print('NO')
