# cook your dish here
t = int(input())
for i in range(t):
    x1, y1, x2, y2 = [int(i) for i in input().split()]
    if x1**2 + y1**2 < x2**2 + y2**2:
        print('A IS CLOSER')
    else:
        print('B IS CLOSER')
