def row_sum_odd_numbers(n):
    # return (1+(n-1)*n) * n + (n-1)*(n)
    # ^ found with logic of - first digit of row * width of row * sum of recursive sequence a(n)=0,2,6,12...
    # with n starting at 0
    # simplify the polynomial expression to n^3
    # feel bad for not seeing the pattern in the first place
    return n**3
