def stringify(node):

    def get(node, L=[]):
        while node:
            (L, node) = (L + [str(node.data)], node.next)
        return L
    return ' -> '.join(get(node) + ['None'])
