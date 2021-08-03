count = 0


def hotpo(n):
    nonlocal count
    if n == 1:
        x = count
        count = 0
        return x
    else:
        if(n % 2 == 0):
            count += 1
            return hotpo(n / 2)
        else:
            count += 1
            return hotpo(3 * n + 1)
