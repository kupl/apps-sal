def digitize(n):
    num_list = list(str(n))
    reversed_num_list = num_list.reverse()
    reversed_num_list = list(map(int, num_list))
    return reversed_num_list
