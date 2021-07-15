def row_sum_odd_numbers(n):
    if n == 1:
        return 1
    my_list = list(range(1,n*(n+1),2))
    return sum(my_list[n*-1:])

