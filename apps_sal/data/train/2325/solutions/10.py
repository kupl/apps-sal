from itertools import accumulate
s = list(input().replace('A', '1').replace('B', '2'))
t = list(input().replace('A', '1').replace('B', '2'))
s = list(map(int, s))
t = list(map(int, t))
accs = [0] + list(accumulate(s))
acct = [0] + list(accumulate(t))
q = int(input())
abcd = [list(map(int, input().split())) for i in range(q)]
for (a, b, c, d) in abcd:
    if (accs[b] - accs[a - 1]) % 3 == (acct[d] - acct[c - 1]) % 3:
        print('YES')
    else:
        print('NO')
