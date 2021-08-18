import math


def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False


for KK_KK in range(eval(input())):

    a = eval(input())
    k = is_square(a)
    if k == True:
        print("YES")
    else:
        print("NO")
