def difference_of_squares(n):
    sumOfSquares = 0
    sum = 0
    for x in range (1, n+1):
        sumOfSquares += x*x
        sum += x
    return sum*sum - sumOfSquares
