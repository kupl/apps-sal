t = int(input())


def prime(n):
    for i in range(2, int(n / 2) + 1):
        if(n % i == 0):
            return 0
    else:
        return 1


for k in range(t):
    line = input().split()
    x = int(line[0])
    y = int(line[1])
    s = x + y + 1
    c = 1
    while (1):
        if (prime(s) == 0):
            c = c + 1
            s = s + 1
        else:
            print(c)
            break
