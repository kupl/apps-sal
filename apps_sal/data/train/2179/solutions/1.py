(a, b, c) = list(map(int, input().split(' ')))
n = int(input())
l = list(map(int, input().split(' ')))
res = 0
for x in l:
    if x > b and x < c:
        res += 1
print(res)
