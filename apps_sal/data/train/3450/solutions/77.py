def array(string):
    # convert string in list
    string_to_list = string.split(",")
    # remove first and last item
    remove_item = string_to_list[1:-1]
    # convert list in string
    result = " ".join(remove_item)
    # control string is not only spaces
    if result.isspace() is True or result == '':
        return None
    else:
        return result
