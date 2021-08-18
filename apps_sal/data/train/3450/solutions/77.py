def array(string):
    string_to_list = string.split(",")
    remove_item = string_to_list[1:-1]
    result = " ".join(remove_item)
    if result.isspace() is True or result == '':
        return None
    else:
        return result
