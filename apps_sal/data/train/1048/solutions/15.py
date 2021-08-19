T = int(input())
for j in range(T):

    ak = input()

    ip1 = ak.split(" ")

    # print(ip1)
    a = float(ip1[0])
    k = float(ip1[1])
    x = input()

    ip2 = list(map(int, x.split()))
    ip2.sort()
    x1 = float(ip2[0])
    x2 = float(ip2[1])
    x3 = float(ip2[2])

    X1 = x1 + a / 2 + k
    X3 = x3 - a / 2 - k
    # print(X1,X3)
    if(X1 >= X3):

        if(x3 - 2 * k - x1 <= 0):
            area = a * a
        else:
            a1 = X1 - X3
            area = a1 * a

    else:
        area = 0
    print("{0:.2f}".format(float(area)))
