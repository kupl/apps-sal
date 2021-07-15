def camel_case(string):
    if len(string) == 0: return ""
    str_list = list(string)
    space_ids = [index for index, char in enumerate(str_list) if char == " " and index < len(str_list) - 1 ]
    for index in space_ids:
        str_list[index + 1] = str_list[index + 1].upper()
    str_list[0] = str_list[0].upper()
    changed_str = "".join(str_list)
    changed_str = changed_str.replace(" ", "")
    return changed_str
