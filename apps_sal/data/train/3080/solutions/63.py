def who_is_paying(name):
    final_list = [name]
    if len (name) <= 2:
        return final_list
    if len(name) > 2:
        name_list = list(name)
        final_list.append(str(name_list[0] + name_list[1]))
        return final_list
