t = int(input())
for i in range(0, t):
    a = int(input())
    r = 1
    count = 0
    while r < a:
        r *= 2
        count += 1
    min = count
    r = 1
    sum = a
    sumr = 1
    count = 0
    while sumr <= sum:
        r *= 2
        sumr += r
        sum += a
        count += 1
    max = count
    print(max, end=' ')
    print(min)
