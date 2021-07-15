def row_sum_odd_numbers(n):
    odd_list = [1]
    max_odd = 1
    for x in range(1, n + 1):
        if x > 1:
            max_odd = max(odd_list)
            odd_list = [y for y in range(max_odd + 2, (max_odd + (2*x) + 2), 2)]
            
    return sum(odd_list)

