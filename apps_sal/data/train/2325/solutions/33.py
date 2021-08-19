from itertools import accumulate, chain
s = input()
t = input()
s_acc = list(chain((0,), accumulate((1 if c == 'A' else -1 for c in s))))
t_acc = list(chain((0,), accumulate((1 if c == 'A' else -1 for c in t))))
q = int(input())
for _ in range(q):
    (a, b, c, d) = list(map(int, input().split()))
    x = s_acc[b] - s_acc[a - 1]
    y = t_acc[d] - t_acc[c - 1]
    print('YES' if x % 3 == y % 3 else 'NO')
