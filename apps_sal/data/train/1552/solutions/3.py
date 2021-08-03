import math
amb = math.factorial(10)
t = eval(input())
asa = pow(10, 10)
li = []
for i in range(t):
    amb2 = math.factorial(10)
    a, b, c = list(map(int, input().split()))
    asa2 = pow(10, 10)
    d = (c * (c + 1)) / 2
    if d <= a and d <= b:
        li.append(a + b - 2 * d)
    else:
        amb2 = math.factorial(10)
        x = abs(a - b)
        li.append(x)
for i in li:
    print(i)
