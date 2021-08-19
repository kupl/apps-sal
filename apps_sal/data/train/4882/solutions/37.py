def round_to_next5(n):
    if n % 5 == 0:
        return n
    else:
        res = 0
        while (n + res) % 5:
            res += 1
        return n + res
