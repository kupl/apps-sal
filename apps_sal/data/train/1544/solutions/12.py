T = int(input())

for t in range(T):
    N = int(input())

    for i in range(N):
        if(i == 0):
            print("*")
        elif(i == (N - 1)):
            print("*" * N)
        else:
            print("*" + " " * (i - 1) + "*")
