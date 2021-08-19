def difference_of_squares(n):
    sq_sums = 0
    sum_sqs = 0
    for i in range(1, n + 1):
        sq_sums += i ** 2
    for j in range(1, n + 1):
        sum_sqs += j
    return sum_sqs ** 2 - sq_sums
