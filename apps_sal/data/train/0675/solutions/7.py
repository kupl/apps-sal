def powerf(P):
    return P != 0 and P & P - 1 == 0


test = int(input())
for i in range(test):
    N = int(input())
    if N == 1:
        print(N)
        continue
    elif N == 3:
        print(1, 3, 2)
        continue
    elif N == 5:
        print(2, 3, 1, 5, 4)
    elif powerf(N):
        print(-1)
        continue
    else:
        print(2, 3, 1, 5, 4)
        i = 6
        while i <= N:
            if powerf(i):
                print(i + 1, i)
                i = i + 2
            else:
                print(i)
                i = i + 1
