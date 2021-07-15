def find_multiples(integer, limit):
    final_list = []
    for i in range(integer, limit + 1):
        if i % integer == 0:
            final_list.append(i)
    return final_list
