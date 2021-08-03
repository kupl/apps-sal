for _ in range(int(input())):
    x = int(input())

    n = 0
    t = 0
    while(n < x):
        n = 2**t
        t += 1
    print(2**(t - 1))
