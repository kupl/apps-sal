class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def length(node):
    i = 0
    while node != None:
        i += 1
        node = node.next
    return i


def count(node, data):
    res = 0
    while node != None:
        res += node.data == data
        node = node.next
    return res
