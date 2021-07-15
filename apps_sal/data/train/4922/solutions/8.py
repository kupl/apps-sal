def list_to_array(node):
    return [] if node is None else [node.value] + list_to_array(node.next)
