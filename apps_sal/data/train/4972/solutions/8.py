class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
    
def length(node):
  return 0 if node == None else 1 if node.next == None else 1 + length(node.next)
  
def count(node, data):
  return 0 if node == None else int(node.data == data) if node.next == None else int(node.data == data) + count(node.next, data)
