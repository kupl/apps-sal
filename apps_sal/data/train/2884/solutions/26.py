def stringify(node):
    final = ''
    try:
        final += str(node.data) + ' -> '
        while node.next:
            final += str(node.next.data)
            final += ' -> '
            node = node.next
    except AttributeError:
        pass
    final += 'None'
    return final
