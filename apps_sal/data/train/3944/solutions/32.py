def sum_triangular_numbers(n):
    new_num = 0
    new_num_list =[]
    for num in range(1, n+1):
        new_num += num
        new_num_list.append(new_num)
        print(new_num)
    return sum(new_num_list)

print(sum_triangular_numbers(6))
