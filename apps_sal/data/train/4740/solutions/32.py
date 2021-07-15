def row_sum_odd_numbers(n):
    start = sum(range(1,n))
    end = start + n
    return sum([ i for i in range(1,end*2,2) ][start:end])
