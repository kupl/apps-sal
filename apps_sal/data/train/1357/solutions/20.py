for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    cashier = {5: 0, 10: 0}
    boo = False
    for coin in coins:
        if coin == 5:
            cashier[5] += 1
        elif coin == 10:
            if cashier[5] > 0:
                cashier[5] -= 1
                cashier[10] += 1
            else:
                boo = True
                break
        elif cashier[10] > 0:
            cashier[10] -= 1
        elif cashier[5] >= 2:
            cashier[5] -= 2
        else:
            boo = True
            break
    if boo:
        print('NO')
    else:
        print('YES')
