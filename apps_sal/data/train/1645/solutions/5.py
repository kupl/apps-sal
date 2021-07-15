def sum_of_squares(n):
        import math
        while n % 4 == 0: n = n // 4
        if n % 8 == 7: return 4
        if int(math.sqrt(n)) ** 2 == n: return 1
        i = 1
        while i*i <= n:
            j = math.sqrt(n - i*i)
            if int(j) == j: return 2
            i += 1
        return 3

