T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    Fives = 0
    Flag = True
    Tens = 0
    for i in A:
        if i == 5:
            Fives = Fives + 1
        elif i == 10:
            if Fives > 0:
                Tens = Tens + 1
                Fives = Fives - 1
            else:
                Flag = False
        else:
            if Tens > 0:
                Tens = Tens - 1
            elif Fives > 1:
                Fives = Fives - 2
            else:
                Flag = False
                break
    if Flag == True:
        print('YES')
    else:
        print("NO")
