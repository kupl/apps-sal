def remove_char(s):
    list1 = list(s)
    list1.pop(-1)
    list1.pop(0)
    return "".join(list1) 
