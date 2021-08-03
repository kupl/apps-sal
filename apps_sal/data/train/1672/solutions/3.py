import math

arr = [0 for _ in range(11)]

for x in range(11):
    arr[10 - x] = int(input())

for x in arr:
    tmp = math.sqrt(abs(x)) + (x**3) * 5
    if tmp >= 400:
        print("f({}) = MAGNA NIMIS!".format(x))
    else:
        print("f({}) = {:.2f}".format(x, round(tmp, 2)))
