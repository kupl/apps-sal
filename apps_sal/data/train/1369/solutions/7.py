from math import sqrt
t = int(input())
for _ in range(t):
    n = int(input())
    sum = 0
    if n < 2:
        pass
    elif n == 2:
        sum = 2
    else:
        sum = 2
        for no in range(3, n + 1, 2):
            for odd in range(3, int(sqrt(no)) + 1, 2):
                if no % odd == 0:
                    break
            else:
                sum += no
    print(sum)
