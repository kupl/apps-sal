class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def length(node, filter=None):
    l = 0
    while node != None:
        node, l = node.next, l + (filter is None or filter == node.data)
    return l


def count(node, data): return length(node, data)
