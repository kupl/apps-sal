t = int(input())
for i in range(t):
    (x, y, z) = list(map(int, input().split()))
    if (x > y and x < z) or (x > z and x < y):
        print(x)
    elif (y > x and y < z) or (y > z and y < x):
        print(y)
    else:
        print(z)  # cook your dish here
