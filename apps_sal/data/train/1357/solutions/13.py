for _ in range(int(input().strip())):
    N = int(input().strip())
    A = list(map(int, input().strip().split(" ")))
    coins = [0, 0, 0]
    f = 1
    for i in A:
        #print(i, coins)
        if i == 5:
            coins[0] += 1
        elif i == 10 and coins[0] > 0:
            coins[0] -= 1
        elif i == 15:
            if coins[1] > 1:
                coins[1] -= 1
            elif coins[1] > 1:
                coins[1] -= 2
            else:
                f = 0
                print("NO")
                break
        else:
            f = 0
            print("NO")
            break
    if f:
        print("YES")
