(n, d) = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
total = 0
position = 2
for i in range(n - 2):
    l = x[i]
    distance = 1
    for j in range(position, n):
        if x[j] - l > d:
            distance = j - i - 1
            position = j
            break
    else:
        distance = n - i - 1
        position = n
    total += distance * (distance - 1) // 2
print(total)
