from math import floor

a = [0, 1, 2, 4, 6]
for i in range(1, 70):
    a.append(a[i] * 12)


b = []

for i in range(len(a)):
    b.append([a[i], i % 4])

# print b


def func(x):
    tot = 0
    for i in range(len(x)):
        for j in range(len(b) - 1):
            if x[i] >= b[j][0] and x[i] < b[j + 1][0]:
                # print tot,b[j][1]
                tot ^= b[j][1]
                break

    return tot


t = eval(input())
for i in range(t):
    n = eval(input())
    x = list(map(int, input().split()))
    if func(x) == 0:
        print("Derek")
    else:
        print("Henry")
