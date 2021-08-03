n = int(input())
while n > 0:
    i = 1
    a, b = (int(i) for i in input().split())
    if (b + 1) % (i << a) == 0:
        print("ON")
    else:
        print("OFF")
    n = n - 1
