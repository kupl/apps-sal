def list_to_array(lst):
    array = []
    while lst:
      array.append(lst.value)
      lst = lst.next
    return array
