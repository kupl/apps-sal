def string_func(in_str, action_times):
    input_len = len(in_str)
    input_mid_point = (input_len + 1) / 2 - 1
    loops = [[0]]
    index = 0
    loop_index_is_in = [0] * input_len
    indices_not_checked = list(range(1, input_len))
    while len(indices_not_checked) != 0:
        if index < input_mid_point:
            index = index * 2 + 1
        elif index > input_mid_point:
            index = (input_len - 1 - index) * 2
        elif index == input_mid_point:
            index = input_len - 1
        if index not in indices_not_checked:
            loops.append([])
            index = indices_not_checked[0]
        loops[-1].append(index)
        indices_not_checked.remove(index)
        loop_index_is_in[index] = len(loops) - 1
    new_string = [0] * input_len
    for char_index in range(input_len):
        loop = loops[loop_index_is_in[char_index]]
        place_in_loop = loop.index(char_index)
        new_index = loop[(place_in_loop + action_times) % len(loop)]
        new_string[new_index] = in_str[char_index]
    return ''.join(new_string)
