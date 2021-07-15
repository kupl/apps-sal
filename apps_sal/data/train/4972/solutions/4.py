class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    n = node
    len = 0
    while n is not None:
        len += 1
        n = n.next
    return len
  
def count(node, data):
    n = node
    count = 0
    while n is not None:
        if data == n.data:
            count += 1
        n = n.next
    return count
