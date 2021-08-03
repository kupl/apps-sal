def powers_of_two(n):
    power = n
    square_list = [1]
    for i in range(1, n + 1):
        square_list.append(2 ** i)
    return square_list
