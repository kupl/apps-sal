from collections import defaultdict
t = int(input())
for _ in range(t):
    s = input()
    s = list(s)
    l = s[:]
    n = len(s)
    ans = 0
    if n <= 100:
        l = []
        for i in range(n):
            for j in range(i + 1, n):
                l.append(s[i:j])
        ans = 0
        for i in l:
            dic = defaultdict(lambda: 0)
            for j in i:
                dic[j] += 1
            cnt = 0
            for k in dic.keys():
                if dic[k] % 2 == 1:
                    cnt += 1
            if cnt <= 1:
                ans = max(ans, len(i))
        print(ans)
        continue
    for i in range(n):
        dic = defaultdict(lambda: 0)
        unmatched = 0
        for j in range(i, n):
            dic[l[j]] += 1
            if dic[l[j]] % 2 == 1:
                unmatched += 1
            else:
                unmatched -= 1
            if unmatched <= 1:
                ans = max(ans, j - i + 1)
    print(ans)
