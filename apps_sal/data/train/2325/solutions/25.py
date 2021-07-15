from itertools import accumulate
import sys
readlines = sys.stdin.readlines
input = sys.stdin.readline
S = tuple(accumulate([1 if x == 'A' else 2 for x in input().rstrip()]))
T = tuple(accumulate([1 if x == 'A' else 2 for x in input().rstrip()]))
input()
for line in readlines():
    a, b, c, d = [int(x)-1 for x in line.split()]
    s = S[b]-S[a-1] if a else S[b]
    t = T[d]-T[c-1] if c else T[d]
    print(('YES' if s % 3 == t % 3 else 'NO'))

