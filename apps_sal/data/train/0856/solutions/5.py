# cook your dish here
from collections import defaultdict
for _ in range(int(input())):
    mp = defaultdict(lambda: 0)
    sat = set()
    for _ in range(int(input())):
        w, s = input().split()
        mp[w, s] += 1
        sat.add(w)
    ans = 0
    for i in sat:
        ans += max(mp[i, '0'], mp[i, '1'])
    print(ans)
