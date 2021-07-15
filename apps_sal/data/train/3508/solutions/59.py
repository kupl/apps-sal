def halving_sum(n):
    i, sum = 2, n
    while(i <= n):
        sum += n//i
        i += i
    return sum
