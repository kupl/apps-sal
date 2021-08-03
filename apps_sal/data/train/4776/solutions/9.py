
def length_sup_u_k(n, k):
    greater_num = 0

    number_table = []
    for index in range(0, n):
        if index <= 1:
            number_table.append(1)
        else:
            first_index = number_table[index - 1]
            last_index = number_table[index - 2]
            new_number = number_table[index - first_index] + number_table[index - last_index]
            number_table.append(new_number)
        if number_table[index] >= k:
            greater_num += 1
    return greater_num


def comp(n):
    pred_suck_count = 0
    number_table = []
    for index in range(0, n):
        if index <= 1:
            number_table.append(1)
            continue
        else:
            first_index = number_table[index - 1]
            last_index = number_table[index - 2]
            new_number = number_table[index - first_index] + number_table[index - last_index]
            number_table.append(new_number)
        if number_table[index] < number_table[index - 1]:
            pred_suck_count += 1

    return pred_suck_count
