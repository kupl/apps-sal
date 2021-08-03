def who_is_paying(name):
    if len(name) > 2:
        list = []
        for char in name:
            list.append(char)

        a = ''
        a += list[0]
        a += list[1]
        list2 = []
        list2.append(name)
        list2.append(a)
        return list2
    else:
        list = []
        list.append(name)
        return list
