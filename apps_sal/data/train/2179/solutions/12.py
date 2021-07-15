a, b, c = list(map(int, input().split()))
n = int(input())
xs = list(map(int, input().split()))

cnt = 0
for x in xs:
    cnt += int(b < x and x < c)
print(cnt)

