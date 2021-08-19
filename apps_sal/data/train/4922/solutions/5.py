def list_to_array(l):
    return list() if l == None else [l.value] + list_to_array(l.next)
