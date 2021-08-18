try:
    import math

    def getSum(arr, n):

        fact = math.factorial(n)

        digitsum = 0
        for i in range(n):
            digitsum += arr[i]
        digitsum *= (fact // n)

        res = 0
        i = 1
        k = 1
        while i <= n:
            res += (k * digitsum)
            k = k * 10
            i += 1

        return res

    b = int(input())

    ls = []

    while(b > 0):
        a = int(input())

        arr = input()
        l = list(map(int, arr.split(' ')))

        b -= 1
        n = len(l)
        n = a

        g = int(getSum(l, n))
        ls.append(g)
    for i in ls:
        print(i)
except:
    pass
