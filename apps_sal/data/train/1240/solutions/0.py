t = int(input())
while t:
    x = int(input())
    arr = [int(i) for i in input().split()]
    total = 0
    for i in arr:
        if i % 6 == 0:
            total += 6
        else:
            total += (i % 6)
    print(total)
    t -= 1
