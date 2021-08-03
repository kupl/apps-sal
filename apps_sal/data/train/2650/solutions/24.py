n, l = map(int, input().split())
s = [input() for _ in range(n)]
an = ''
for _ in range(n):
    an += min(s)
    s.remove(min(s))
print(an)
