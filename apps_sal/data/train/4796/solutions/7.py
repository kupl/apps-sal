class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def get_nth(node, index):
    # Your code goes here.
    if node is None or index < 0:
        raise LookupError('invalid index')
    for i in range(index):
        if node.__next__ is None:
            raise IndexError('index out of range')
        node = node.__next__
    return node
