def difference_of_squares(n):
    rng = []
    sqs = []
    for i in range(1, n + 1):
        rng.append(i)
        sqs.append(i ** 2)
    return sum(rng) ** 2 - sum(sqs)
