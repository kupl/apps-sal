class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    leng = 0
    while node:
        leng += 1
        node = node.next
    return leng
  
def count(node, data):
    c = 0
    while node:
        if node.data==data:
            c += 1
        node = node.next
    return c
