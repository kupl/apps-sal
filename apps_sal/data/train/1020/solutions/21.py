for _ in range(int(input().strip())):
    (n, k) = list(map(int, input().strip().split()))
    total = 0
    player = 0
    for i in map(int, input().strip().split()):
        if player == 0:
            if total < 0:
                total -= i
            else:
                total += i
            player = 1
        else:
            if total < 0:
                total += i
            else:
                total -= i
            player = 0
    if abs(total) >= k:
        print(1)
    else:
        print(2)
