from itertools import accumulate

*S, = [1 if x == 'A' else 2 for x in input()]
*T, = [1 if x == 'A' else 2 for x in input()]

acc_s = (0,) + tuple(accumulate(S))
acc_t = (0,) + tuple(accumulate(T))

Q = int(input())
for _ in range(Q):
    sl, sr, tl, tr = list(map(int, input().split()))
    sl -= 1
    tl -= 1
    diff = (acc_t[tr] - acc_t[tl]) - (acc_s[sr] - acc_s[sl])
    print(('YES' if diff % 3 == 0 else 'NO'))
