import math


def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return "YES"
    else:
        return "NO"


for i in range(eval(input())):
    n = eval(input())
    print(is_square(n))
