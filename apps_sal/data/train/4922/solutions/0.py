def list_to_array(lst):
    arr = []
    while lst != None:
        arr.append(lst.value)
        lst = lst.next
    return arr
