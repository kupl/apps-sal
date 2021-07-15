def find_multiples(integer, limit):
    my_list = []
    for i in range(integer,limit + 1):
        if i % integer == 0:
            my_list.append(i)
    return my_list

