# cook your dish here
T = int(input())
for i in range(T):
    K = int(input())
    if K == 1:
        print("*")
    else:
        print("*")
        L = K - 1
        while(L > 0):
            i = 1
            if L == 1:
                print("*" * (2 * K - 1))
            else:
                print("*" + " " * i + "*")
                i += 2
            L = L - 1
