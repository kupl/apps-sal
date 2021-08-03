import math

a = [int(input()) for i in range(11)][::-1]
for i in a:
    p = i ** 3 * 5 + math.sqrt(abs(i))
    if p >= 400.:
        print("f({}) = MAGNA NIMIS!".format(i))
    else:
        print("f({}) = {:.2f}".format(i, p))
