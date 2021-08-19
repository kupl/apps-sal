# cook your dish here
def fuck_off(x, y):
    X = bin(x + 1)[2:]
    Y = bin(y + 1)[2:]
    count1, count2 = 0, 0
    for i in X:
        if i == '1':
            count1 += 1
    for i in Y:
        if i == '1':
            count2 += 1
    if count1 == count2:
        print(0, " ", 0)
    if count1 > count2:
        print(2, " ", abs(count1 - count2))
    if count1 < count2:
        print(1, " ", abs(count2 - count1))


t = int(input())
for i in range(t):
    x, y = input().split()
    fuck_off(int(x), int(y))
