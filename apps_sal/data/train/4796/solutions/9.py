class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def get_nth(node, index):
    assert(node and index >= 0)
    for _ in range(index):
        node = node.next
        assert(node)
    return node
