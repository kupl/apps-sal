def totient(a):
    try:
        res = max(int(a), 0)
        b = a
        i = 2
        while i * i <= a:
            if a % i == 0:
                res -= res // i
                while a % i == 0:
                    a //= i
            i = i + 1
        if(a > 1):
            res -= res // a
        return res
    except:
        return 0
