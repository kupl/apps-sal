class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    current = head
    if head is None or head.data > data:
        return push(head, data)
    while current.next is not None and data > current.next.data:
        current = current.next
    current.next = push(current.next, data)
    return head
