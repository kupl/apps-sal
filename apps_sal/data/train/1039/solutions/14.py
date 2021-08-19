try:
    t = int(input())
    while t:
        (x, y) = input().split()
        x = int(x)
        y = int(y)
        if x == y:
            print(0)
        elif x < y and (y - x) % 2 == 1 or (x > y and (x - y) % 2 == 0):
            print(1)
        elif x < y and (y - x) % 4 == 0:
            print(3)
        elif x > y and (x - y) % 2 == 1 or (x < y and (y - x) % 2 == 0):
            print(2)
        t -= 1
except:
    pass
