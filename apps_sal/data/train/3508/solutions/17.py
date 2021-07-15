def halving_sum(n):
    result = n

    if n < 1:
        return n
    else:
        while n > 1:
            result += n // 2
            n = n // 2
        return result

print((halving_sum(25)))

