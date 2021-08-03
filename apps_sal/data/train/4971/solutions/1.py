class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    if head is None or head.data > data:
        return push(head, data)

    current = head
    while current.next and data > current.next.data:
        current = current.next

    current.next = push(current.next, data)
    return head
