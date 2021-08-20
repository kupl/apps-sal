class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def get_nth(node, index):
    if node is None or index < 0:
        raise Exception('Invalid parameters.')
    while index > 0:
        if node.__next__ is None:
            raise Exception('Null node encountered.')
        node = node.__next__
        index -= 1
    return node
