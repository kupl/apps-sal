T = int(input())

while T > 0:
    Out = 0
    summ = 0
    Res = 0
    N = int(input())
    M = N
    leng = len(str(N))

    for i in range(0, leng):
        Res = N % 10
        Out = pow(Res, leng)
        summ = summ + Out
        N = N // 10
    if summ == M:
        print("FEELS GOOD")
    else:
        print("FEELS BAD")
    T = T - 1
