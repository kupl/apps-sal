import math
try:
    def prime(n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    for t in range(int(input())):
        x, y = list(map(int, input().split()))
        s = x + y
        i = s
        while(1):
            if prime(s + 1):
                ans = s + 1
                break
            else:
                s += 1
        print(ans - i)

except:
    pass
