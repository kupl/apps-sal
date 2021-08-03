def increment_string(strng):
    numeric_str = ''
    for i in reversed(strng):
        if not i.isdigit():
            break
        if i.isdigit():
            numeric_str += i

    if(numeric_str == ''):
        return strng + '1'
    else:
        numeric_str = numeric_str[::-1]
        str_num = str(int(numeric_str) + 1)
        return strng[:-len(numeric_str)] + '0' * (len(numeric_str) - len(str_num)) + str_num
