class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def count_if(node, fn):
    n, c = node, 0
    while n:
        if fn(n):
            c += 1
        n = n.next
    return c


def length(node):
    return count_if(node, lambda x: x != None)


def count(node, data):
    return count_if(node, lambda x: x.data == data)
