for _ in range(int(input())):
    K = int(input())
    if K == 1:
        print('*')
    elif K == 2:
        print(" * ")
        print("***")
    else:
        a = K - 1
        s = K - 2
        print(" " * (s + 1) + "*")
        for i in range(1, K - 1):
            print(" " * s + "*" + " " * ((a - s) * 2 - 1) + "*")
            s -= 1
        print("*" * (K * 2 - 1))
