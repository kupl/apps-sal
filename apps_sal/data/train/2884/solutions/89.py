def stringify(node):
    if node == None:
        return "None"
    to_remove = "(),"
    table = {ord(char): None for char in to_remove}
    head = int(node.data)
    tail = node.__next__
    if tail == None:
        return str((" -> ".join((str(head), "None"))).translate(table))
    else:
        return str((" -> ".join((str(head), stringify(tail)))).translate(table))
