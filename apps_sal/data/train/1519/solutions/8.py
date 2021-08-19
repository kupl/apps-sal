try:
    x = int(input())
    for _ in range(x):
        a = int(input())
        i = 0
        while 2 ** i < a:
            i += 1
        print(2 ** i)
except:
    pass
