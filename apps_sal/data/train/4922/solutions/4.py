def list_to_array(lst):
    list = []
    while lst is not None:
        list.append(lst.value)
        lst = lst.__next__
    return list
        

