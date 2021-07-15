def sum_of_minimums(n):
    sum=0
    for i in n:
        sum+=min(i)
    return sum
