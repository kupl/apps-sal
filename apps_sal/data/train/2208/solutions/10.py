from sys import stdin
n, k = tuple(int(x) for x in stdin.readline().split())
dic = {}
ans = 0
for i in range(k):
    a, b = tuple(int(x) for x in stdin.readline().split())
    a -= 1
    b -= 1
    if a not in dic:
        dic[a] = set((b,))
    else:
        dic[a].add(b)

    if b not in dic:
        dic[b] = set((a,))
    else:
        dic[b].add(a)

for i in range(n):
    if i in dic:
        lst = [i]
        s = set((i,))
        for src in lst:
            if src in dic:
                for dest in dic[src]:
                    if dest in dic and dest not in s:
                        lst.append(dest)
                        s.add(dest)
                        ans += 1
                del dic[src]
print(k - ans)
