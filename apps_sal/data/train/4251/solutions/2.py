def difference_of_squares(x):

    # Initialize
    square_sum = 0
    sum_squares = 0

    # Loop over x numbers to create the sum and add all squares
    for i in range(1, x + 1):
        square_sum += i
        sum_squares += i**2

    # Power the sum of the x values
    square_sum **= 2

    # Return the difference
    return (square_sum - sum_squares)
