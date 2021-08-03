a, b, c = list(map(int, input().split()))
n = int(input())
xs = list(map(int, input().split()))
count = 0
for x in xs:
    if b < x < c:
        count += 1
print(count)
