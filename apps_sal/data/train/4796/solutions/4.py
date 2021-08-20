class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):
    if not head:
        return 0
    else:
        length = 0
        current_node = head
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length


def get_nth(head, index):
    if not head:
        raise ValueError('Head node cannot be None')
    if index < 0:
        raise ValueError('Index cannot be negative')
    if index > length(head) - 1:
        raise ValueError('Index cannot exceed number of nodes in list')
    counter = 0
    current_node = head
    while counter != index:
        current_node = current_node.next
        counter += 1
    return current_node
