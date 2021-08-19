def stringify(node, output_array=None):
    if output_array is None:
        output_array = []
    if not node:
        output_array.append('None')
    while node:
        output_array.append(node.data)
        return stringify(node.__next__, output_array)
    return ' -> '.join((str(i) for i in output_array))
