class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
    
def get_nth(node, index):
  if node and index >= 0: return node if index < 1 else get_nth(node.next, index - 1)
  raise ValueError
