def sum_triangular_numbers(n):
    #your code here
    count = 0
    sum = 0
    total = 0
    for index in range(n):
        count += 1
        sum += count
        total += sum
    return total
