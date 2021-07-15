def array(string):
    stripped_string_array = string.split(',')[1:-1]
    if len(stripped_string_array) == 0:
        return None

    return " ".join(stripped_string_array)

