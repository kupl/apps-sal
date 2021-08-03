def powers_of_two(n):
    if n == 0:
        return [1]
    num = 1
    my_list = [num]
    for i in range(1, (n + 1)):
        num = num * 2
        my_list.append(num)
    return my_list
