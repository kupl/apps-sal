def row_sum_odd_numbers(n):
    m = (1+n)*n/2
    l = 1+(m-1)*2
    q = (1+l)*m/2
    p = (1+1+(m-n-1)*2)*(m-n)/2
    return q-p
