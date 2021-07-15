list_to_array = lambda l: list() if l == None else [l.value] + list_to_array(l.next)
