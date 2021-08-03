def halving_sum(n):
    my_list = []
    while n:
        my_list.append(n)
        n = n // 2
    return sum(my_list)
