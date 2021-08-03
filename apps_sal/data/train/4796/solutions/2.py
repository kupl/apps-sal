class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def get_nth(node, index, i=0):
    if node is None:
        raise IndexError
    else:
        return node if index == i else get_nth(node.__next__, index, i + 1)
