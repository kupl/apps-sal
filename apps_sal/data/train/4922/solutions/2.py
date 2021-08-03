def list_to_array(ll):
    output = []
    while ll:
        output.append(ll.value)
        ll = ll.__next__
    return output
