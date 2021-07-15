class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def iterlinkedlist(node):
    while node:
        yield node
        node = node.next

def length(node):
    return sum(1 for n in iterlinkedlist(node))

def count(node, data):
    return sum(n.data == data for n in iterlinkedlist(node))
