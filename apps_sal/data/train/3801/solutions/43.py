import string


def words_to_marks(input_str):
    values = dict(list(zip(string.ascii_lowercase, list(range(1, 27)))))
    input_lst = list(input_str)
    value = 0
    for elem in input_lst:
        value += values[elem]
    return value
