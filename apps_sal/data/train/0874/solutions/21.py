# cook your dish here
import math
x = int(input())

for i in range(x):

    a, b, c = map(int, input().strip().split())
    s = [int(i) for i in input().strip().split()]
    s.sort()
    m = 0
    counter = 0
    for i in range(a):
        a1 = math.ceil((s[i] / c))
        if(b >= a1 and a1 <= 2):
            counter += 1
            b = b - a1
        else:
            break

    print(counter)
