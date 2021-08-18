t = int(input())
while(t > 0):
    x, y = map(int, input().split())
    res = 1
    i = 1
    strength = 0
    while((y * i) <= x):
        res = y * i
        strength += (res % 10)

        i += 1
    print(strength)
    t -= 1
