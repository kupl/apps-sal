class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(node):
    k = ''
    while True:
        if node == None:
            k += 'None'
            return k
        else:
            k += '{} -> '.format(node.data)
            node = node.next
