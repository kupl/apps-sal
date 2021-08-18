try:
    def isprime(n):
        if n == 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        j = 5
        while(j * j <= n):
            if n % j == 0 or n % (j + 2) == 0:
                return False
            j += 6
        return True
    test = int(input())
    for i in range(test):
        n = int(input())
        s = 0
        for j in range(1, n + 1):
            if(isprime(j)):
                s += j
        print(s)
except Exception as e:
    print(e)
