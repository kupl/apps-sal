class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def length(node):
    return 1 + length(node.next) if node else 0


def count(node, data):
    return (1 if node.data == data else 0) + count(node.next, data) if node else 0
