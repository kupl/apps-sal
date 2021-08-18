T = int(input())

for t in range(T):
    apples, oranges, coins = input().split()
    apples = int(apples)
    oranges = int(oranges)
    coins = int(coins)
    while coins > 0:
        if apples > oranges:
            oranges += 1
            coins -= 1
        elif oranges > apples:
            apples += 1
            coins -= 1
        else:
            if coins % 2 == 0:
                half = int(coins / 2)
                apples = apples + half
                oranges = oranges + half
                coins = 0
                break
            else:
                half = int(coins / 2)
                apples = apples + half
                oranges = oranges + half
                coins = 1
                break
    print(int(abs(apples - oranges)))
