def who_is_paying(name):
    names_list = [ ]
    if(len(name)<=2):
        names_list.append(name)
        return names_list
    names_list.append(name)
    names_list.append(name[:2])
    return names_list

