(n, l) = map(int, input().split())
strings = []
for _ in range(n):
    s = input()
    strings.append(s)
strings.sort()
ans = ''
for string in strings:
    ans += string
print(ans)
