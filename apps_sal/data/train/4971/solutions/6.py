class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def sorted_insert(head, data):
    
    new_node = Node(data)
    if head == None or data < head.data:
        new_node.next = head
        return new_node
    node = head
    
    while 1:
        if node.next == None or data <= node.next.data:
            new_node.next = node.next
            node.next = new_node
            return head
        node = node.next
