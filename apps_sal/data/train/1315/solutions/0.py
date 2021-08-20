n = int(input())
l = []
count = 0
while n:
    n -= 1
    (a, b, c) = sorted(map(int, input().split()))
    if (a, b, c) in l:
        count -= 1
    else:
        l.append((a, b, c))
        count += 1
print(count)
