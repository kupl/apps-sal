def halving_sum(n):
    total = n
    divisor = 2
    while n // divisor > 0:
        if n // divisor == 1:
            total += 1
            break
        else:
            total += (n // divisor)
            divisor *= 2
    return(total)
