# cook your dish here
import math
count = 0


def steps(num):
    nonlocal count

    expo = int(math.log(num, 2))
    nearPow = int(pow(2, expo))
    if(nearPow == num):
        return count
    num -= nearPow
    count += 1
    if(num == 1):
        return count
    else:
        steps(num)
    return count


iterator = int(input())
while(iterator > 0):
    count = 0
    num = int(input())
    print((steps(abs(num))))
    iterator -= 1
