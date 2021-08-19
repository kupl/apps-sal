for t in range(int(input())):
    (limakMax, bobMax) = list(map(int, input().split()))
    limakEat = 0
    bobEat = 0
    eating = 1
    while limakEat <= limakMax or bobEat <= bobMax:
        if eating % 2 != 0 and limakEat <= limakMax:
            limakEat += eating
            eating += 1
            if limakEat > limakMax:
                print('Bob')
                break
        elif eating % 2 == 0 and bobEat <= bobMax:
            bobEat += eating
            eating += 1
            if bobEat > bobMax:
                print('Limak')
                break
