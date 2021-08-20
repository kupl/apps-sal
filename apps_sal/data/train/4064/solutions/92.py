def count_by(x, n):
    list_result = []
    last_entry = 0
    for i in range(n):
        last_entry += x
        list_result.append(last_entry)
    return list_result
    '\n    Return a sequence of numbers counting by `x` `n` times.\n    '
