def halving_sum(n):
    if n == 1:
        return n
    else:
        print(n)
        return n + halving_sum(n // 2)
