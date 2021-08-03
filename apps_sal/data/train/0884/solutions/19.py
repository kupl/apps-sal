# cook your dish here
T = int(input())
for a in range(T):
    X, K = input().split(" ")
    X = int(X)
    K = int(K)
    s = 0
    su = 0
    for i in range(2, X + 1):
        if(X % i == 0):
            s += i**K

    for i in range(2, K + 1):
        if(K % i == 0):
            su += i * X

    print(s, " ", su)
