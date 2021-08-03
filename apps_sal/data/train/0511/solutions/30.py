n = int(input())
a = list(map(int, input().split(" ")))
mas = 0
for i in a:
    mas ^= i
ans = []
for i in a:
    ans.append(mas ^ i)
print(*ans)
