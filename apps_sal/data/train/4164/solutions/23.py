def first_non_repeating_letter(string):
    check_list = []
    list_string = list(string.lower())
    for let in string:
        if let not in check_list:
            list_string.remove(let.lower())
            check_list.append(let)
            if let.lower() not in list_string:
                return let
    return ''
