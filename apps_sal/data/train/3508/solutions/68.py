def halving_sum(n):
    sum = n
    divide = n
    while divide // 2:
        divide = divide // 2
        sum += divide
    return sum
