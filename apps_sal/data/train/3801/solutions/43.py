import string


def words_to_marks(input_str):

    # Build dictionary of letters and corresponding numbers
    values = dict(list(zip(string.ascii_lowercase, list(range(1, 27)))))

    # Convert input string to list
    input_lst = list(input_str)

    # Get total value for input
    value = 0
    for elem in input_lst:
        value += values[elem]

    return value
