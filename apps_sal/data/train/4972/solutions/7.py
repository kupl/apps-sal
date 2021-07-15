class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    # Your code goes here.
    i = 0
    while node != None:
        i+=1
        node = node.next
    return i
  
def count(node, data):
    # Your code goes here.
    res = 0
    while node != None:
        res+= node.data == data        
        node = node.next
    return res
