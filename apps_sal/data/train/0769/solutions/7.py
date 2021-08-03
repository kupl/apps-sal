def computeGCD(x, y):

    while(y):
        x, y = y, x % y

    return x


for i in range(int(input())):
    a, b = list(map(int, input().split()))
    print(computeGCD(a, b))
