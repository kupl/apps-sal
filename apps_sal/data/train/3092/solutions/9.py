def denumerate(enum_list):
    if type(enum_list) is list:
        tmp = [None] * len(enum_list)

        for index, item in enumerate(enum_list):
            if type(item) is not tuple or len(item) != 2 or not str(item[1]).isalnum() or len(str(item[1])) != 1 or type(item[0]) is not int:
                return False
            try:
                tmp[item[0]] = item[1]
            except:
                return False

        tmp = list(filter(None, tmp))

        if len(tmp) != len(enum_list):
            return False

        return ''.join(tmp)

    return False
