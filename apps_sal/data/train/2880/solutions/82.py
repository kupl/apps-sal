def seven(m):
    step_counter = 0

    while len(list(str(m))) > 2:
        number_list = list(str(m))

        first_part_of_number = int("".join(number_list[:-1])) if len(number_list) > 1 else int(number_list[0])
        second_part_of_number = int(number_list[-1])

        m = first_part_of_number - 2*second_part_of_number

        del number_list[-1]
        step_counter +=1

    return m, step_counter
