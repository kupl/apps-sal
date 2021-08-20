t = int(input())
while t > 0:
    s = int(input())
    while s % 10 == 0:
        s /= 10
    print(''.join(reversed(str(s))))
    t = t - 1
