# cook your dish here
for i in range(int(input())):
    X1, X2, X3, V1, V2 = map(int, input().split())
    D1 = abs(X3 - X1)
    D2 = abs(X3 - X2)
    T1 = D1 / V1
    T2 = D2 / V2
    if T1 > T2:
        print("Kefa")
    elif T2 > T1:
        print("Chef")
    else:
        print("Draw")
