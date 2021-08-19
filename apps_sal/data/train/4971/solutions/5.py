class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def sorted_insert(head, data, node=None):
    if head is None or head.data >= data:
        return Node(data, head)
    if head.data < data:
        head.next = sorted_insert(head.next, data)
        return head
    raise ValueError
