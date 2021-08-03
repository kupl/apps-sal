class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def length(node):
    if node:
        return 1 + length(node.next)
    return 0


def count(node, data):
    if node:
        if node.data == data:
            return 1 + count(node.next, data)
        return count(node.next, data)
    return 0
