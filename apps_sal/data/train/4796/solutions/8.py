class Node(object):
    def __init__(self, data, nxt=None):
        self.data, self.next = data, nxt


def get_nth(node, index):
    i = 0
    while i < index and node:
        node, i = node.next, i + 1
    if node and i == index:
        return node
    raise IndexError
