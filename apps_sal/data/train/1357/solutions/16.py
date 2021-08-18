
for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    res = True
    fives = 0
    tens = 0
    for i in coins:
        if i == 5:
            fives += 1
        elif i == 10:
            if fives > 0:
                fives -= 1
                tens += 1
            else:
                res = False
                break
        else:
            if tens > 0:
                tens -= 1
            elif fives > 1:
                fives -= 2
            else:
                res = False
                break
    if res == True:
        print("YES")
    else:
        print("NO")
