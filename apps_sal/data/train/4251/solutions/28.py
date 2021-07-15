def difference_of_squares(n):
    sum_squares = 0
    sum_num = 0
    for i in range (1, n+1):
        sum_squares = sum_squares + i*i
        sum_num = sum_num +i
    return (sum_num)**2 -(sum_squares) 

