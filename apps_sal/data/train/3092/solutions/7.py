def denumerate(enum_list):
    try:
        string = ''
        enum_list = sorted(enum_list, key=lambda i: i[0])
        for (i, j) in enumerate(enum_list):
            if len(j) == 2 and len(j[1]) == 1 and j[1].isalnum() and (i == j[0]):
                string += j[1]
            else:
                return False
        return string
    except:
        return False
