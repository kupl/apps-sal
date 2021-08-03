from math import*
t = int(input())
while(t != 0):
    a, b, c, d = list(map(int, input().split()))
    if sqrt(pow(a, 2) + pow(b, 2)) > sqrt(pow(c, 2) + pow(d, 2)):
        print('B IS CLOSER')
    else:
        print('A IS CLOSER')
    t -= 1
