class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def get_nth(node, index):
    v = -1
    n = node
    while n:
        v += 1
        if v == index:
            return n
        n = n.next

    raise ValueError
