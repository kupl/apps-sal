class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def get_nth(node, index):
    while index:
        node = node.__next__
        index -= 1

    return node if node else node.data
