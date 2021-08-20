import math
time = int(input())


def check(a, b):
    num = a * b
    count = 0
    r = math.sqrt(num)
    r = int(r)
    if num == r ** 2:
        count = r
    else:
        count = r + 1
    if a == b:
        return count * 2 - 2
    elif a * b == count ** 2:
        return count * 2 - 3
    elif a * b > count * (count - 1):
        return count * 2 - 3
    else:
        return count * 2 - 4


for i in range(time):
    (a, b) = list(map(int, input().split()))
    print(check(a, b))
