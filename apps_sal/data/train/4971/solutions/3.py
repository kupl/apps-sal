class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next


def sorted_insert(head, data):
    return Node(data, head) if not head or data < head.data else Node(head.data, sorted_insert(head.next, data))
