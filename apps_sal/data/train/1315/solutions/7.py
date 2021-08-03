s = []
res = 0
for _ in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()
    s.append(a)
# ss=list(ss)
for _ in range(len(s)):
    if s.count(s[_]) == 1:
        res += 1
print(res)
