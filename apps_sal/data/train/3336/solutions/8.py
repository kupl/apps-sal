def get_sum_of_digits(num):
    my_list = []
    for i in str(num):
        my_list.append(int(i))
    return sum(my_list)
