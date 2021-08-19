# cook your dish here
from collections import Counter
from math import ceil
for _ in range(int(input())):

    d = int(input())
    s = input()
    c = Counter(s)

    re = ceil(0.75 * d)
    ans = 0
    if c['P'] >= re:
        print(ans)
        continue

    for i in range(2, d - 2):

        if s[i] == 'A':

            if (s[i - 2] == 'P' or s[i - 1] == 'P') and (s[i + 2] == 'P' or s[i + 1] == 'P'):
                c['P'] += 1
                ans += 1

            if c['P'] >= re:
                print(ans)
                break

    else:
        print(-1)
