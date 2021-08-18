import math


def isPos(num):
    if num % 2 == 0:
        for i in range(num, 2 * num, 1):
            if ((num**2) - ((i / 2)**2))**(1 / 2) == int(((num**2) - ((i / 2)**2))**(1 / 2)):
                return 'YES'
        return 'NO'
    else:
        for i in range(num + 1, 2 * num, 1):
            if ((num**2) - ((i / 2)**2))**(1 / 2) == int(((num**2) - ((i / 2)**2))**(1 / 2)):
                return 'YES'
        return 'NO'


test = int(input())
for __ in range(test):
    num = int(input())
    print(isPos(num))
