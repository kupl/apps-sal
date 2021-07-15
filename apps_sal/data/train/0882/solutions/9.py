from collections import Counter
for _ in range(int(input())):
    s1 = input();s2 = input()
    c1 = Counter(s1);c2 = Counter(s2)
    ans = 0
    se = set(s1).union(set(s2))
    for i in se:
        ans+= min(c1[i],c2[i])
    print(ans)


