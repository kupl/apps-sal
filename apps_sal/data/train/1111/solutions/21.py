t = int(input())
while t > 0:
    n = int(input())
    lst = list(map(int, input().split()))
    count, count1 = 0, 0
    for i in range(n):
        if lst[i] % 2 == 0:
            count += 1
        else:
            count1 += 1
    print(count * count1)

    t -= 1
