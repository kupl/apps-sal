import math
t = int(input())
for T in range(t):
    xf = int(input())
    (x, y) = (0, 0)
    p = 1
    val = 0
    while x <= xf:
        x = p
        y += p * p
        p = math.ceil(math.sqrt(y))
        val += 1
    print(val - 2)
