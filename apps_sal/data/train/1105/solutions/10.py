t = int(input())
while t:
    n = int(input())
    dish = list(map(int, input().split()))
    (b0, b1) = (0, 0)
    mins = 0
    dish.sort(reverse=True)
    for i in dish:
        if b0 <= b1:
            b0 = b0 + i
        else:
            b1 = b1 + i
    print(max(b0, b1))
    t -= 1
