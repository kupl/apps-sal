def binary_places(num):
    current_num = num
    values_list = []

    if current_num % 2 == 1:
        values_list.append(1)
        current_num -= 1
    else:
        values_list.append(0)

    if current_num > 0:
        cumulative_values = 2

        while cumulative_values <= current_num:
            values_list.insert(0, "?")
            cumulative_values *= 2

    this_place_value = 2 ** (len(values_list) - 1)
    current_place = 0

    while current_num > 1:

        if current_num >= this_place_value:
            values_list[current_place] = 1

            current_num -= this_place_value
            current_place += 1
            this_place_value /= 2
        else:
            values_list[current_place] = 0
            current_place += 1
            this_place_value /= 2

    for index, char in enumerate(values_list):
        if char == '?':
           values_list[index] = 0

    return values_list


def evil(n):
    num_list = binary_places(n)

    if 1 in num_list and num_list.count(1) % 2 == 0:
        return "It's Evil!"
    elif 1 in num_list and num_list.count(1) % 2 == 1:
        return "It's Odious!"

