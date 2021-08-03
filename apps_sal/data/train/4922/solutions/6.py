def list_to_array(lst):
    list = []
    while lst:
        list.append(lst.value)
        lst = lst.next
    return list
