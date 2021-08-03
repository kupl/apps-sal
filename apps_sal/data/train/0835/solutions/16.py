T = int(input())
while (T > 0):
    T -= 1
    N, M = list(map(int, input().split(' ')))
    if N == 1 or M == 1:
        x = max(N, M)
        if x == 1:
            print("No")
        elif x == 2:
            print("Yes")
        else:
            print("No")
    elif M % 2 == 0 or N % 2 == 0:
        print("Yes")
    else:
        print("No")
