from itertools import accumulate
from collections import Counter


def is_dominant(ss):
    wc = Counter(ss)
    for i in wc.values():
        if i > 1:
            return True
    return False


t = int(input())
for _ in range(t):
    (n, q) = map(int, input().split(' '))
    s = input()
    p = []
    if n > 2:
        for i in range(n - 2):
            ss = s[i:i + 3]
            if is_dominant(ss):
                val = 1
            else:
                val = 0
            p.append(val)
        p1 = list(accumulate(p))
    for i in range(q):
        (l, r) = map(int, input().split(' '))
        len = r - (l - 1)
        if n < 3 or len < 3:
            ans = 'NO'
        else:
            sum = p1[r - 3]
            if l > 1:
                sum -= p1[l - 2]
            if sum > 0:
                ans = 'YES'
            else:
                ans = 'NO'
        print(ans)
