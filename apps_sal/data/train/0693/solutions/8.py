try:
    t = int(input())

    for i in range(0, t):
        n = int(input())
        fact = 1

        while(n != 0):
            fact = fact * n
            n -= 1
        print(fact)
except:
    pass
