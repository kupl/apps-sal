class Node(object):
  def __init__(self, data, nxt = None):
    self.data = data
    self.next = nxt
    
def sorted_insert(head, data):
  if not head or data < head.data: return Node(data, head)
  else:
    head.next = sorted_insert(head.next, data)
    return head
