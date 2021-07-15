def list_to_array(node):
    arr = []
    while node:
        arr.append(node.value)
        node = node.next
    return arr
