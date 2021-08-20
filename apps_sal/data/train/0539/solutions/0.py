t = eval(input())
while t != 0:
    t -= 1
    n = eval(input())
    if n % 2 == 0:
        print(n * 4)
    elif n % 4 == 3:
        print(n)
    else:
        print(n * 2)
