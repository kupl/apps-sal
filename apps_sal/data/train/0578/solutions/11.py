import math


def ushijima(x):
    return (n - b * x) * x


t = int(input())
for i in range(t):
    (n, b) = (int(x) for x in input().split())
    y1 = math.floor((math.floor(n / 2)) / b)
    y2 = math.floor((math.ceil(n / 2)) / b)
    y3 = math.ceil((math.floor(n / 2)) / b)
    y4 = math.ceil((math.ceil(n / 2)) / b)
    if y1 == 0 and y2 == 0 and y3 == 0 and y4 == 0:
        print("0")

    else:
        print(max(ushijima(y1), ushijima(y2), ushijima(y3), ushijima(y4)))
