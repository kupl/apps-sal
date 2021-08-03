def race(speed):
    ms = None
    c = 1
    for i in speed:
        if ms == None:
            ms = i
        elif i < ms:
            ms = i
            c = c + 1
    return c


for i in range(int(input())):
    n = int(input())
    speed = list(map(int, input().split()))
    print(race(speed))
