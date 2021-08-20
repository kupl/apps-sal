def capitalize(chars, indices):
    indices.sort()
    result_list = []
    next_index_to_cap = 0
    for (index, char) in enumerate(chars):
        if next_index_to_cap < len(indices) and index == indices[next_index_to_cap]:
            char = char.capitalize()
            next_index_to_cap += 1
        result_list.append(char)
    return ''.join(result_list)
