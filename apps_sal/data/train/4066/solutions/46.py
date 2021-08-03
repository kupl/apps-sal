def string_to_array(s):
    array = []
    tmp_string = ""
    for i in s:
        if i == ' ':
            array.append(tmp_string)
            tmp_string = ""
        else:
            tmp_string = tmp_string + i
    array.append(tmp_string)
    return array
