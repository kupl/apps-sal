class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def get_nth(node, index):
    if not node or index < 0:
        raise ValueError

    while index:
        node = node.__next__
        if not node:
            raise ValueError
        index -= 1

    return node
