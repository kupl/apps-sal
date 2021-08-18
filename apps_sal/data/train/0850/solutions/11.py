def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def gcdlist(l):
    if(len(l) == 1):
        return l[0]
    else:
        num1 = l[0]
        num2 = l[1]
        gcdfinal = gcd(num1, num2)
        for i in range(2, len(l)):
            gcdfinal = gcd(gcdfinal, l[i])
        return(gcdfinal)


for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if(n == 1):
        print(a[0])
    elif(n == 2):
        print(a[0] + a[1])
    else:
        max1 = 0
        max2 = 0
        for i in range(1, n):
            if (a[i] > max1):
                max2 = max1
                max1 = a[i]
            elif (a[i] > max2 and a[i] != max1):
                max2 = a[i]
        a1 = []
        a2 = []
        for i in range(n):
            if(a[i] != max1):
                a1.append(a[i])
            if (a[i] != max2):
                a2.append(a[i])
        if (len(a1) == 0):
            print(a[0])
        else:
            g1 = gcdlist(a1)
            g2 = gcdlist(a2)
            print(max(g1 + max1, g2 + max2))
