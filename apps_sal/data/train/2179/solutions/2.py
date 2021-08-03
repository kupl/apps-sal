a, b, c = map(int, input().split())
n = int(input())
res = 0
for i in map(int, input().split()):
    res += b < i < c
print(res)
