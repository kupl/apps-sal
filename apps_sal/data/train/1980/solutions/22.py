import random

class Node:
  def __init__(self, val, level, count = 1):
    self.val = val
    # list hold refr to nodes on different level
    self.next = [None] * (level + 1)
    # count the number of duplicates of this val
    self.count = count

class Skiplist:

  def __init__(self, p = 0.5):
    # promote probability
    self.p = p
    # head of the skiplist
    self.head = Node(None, 0)
    # num of levels of the skiplist
    self.levels = 1

  def _randomLevel(self):
    # generate a random level
    _level = 0
    while random.random() < self.p:
      _level += 1
    return _level
  
  def _update(self, val):
    # candidate list of node to be updated at each level
    update = [None] * self.levels
    x = self.head
    for i in reversed(list(range(self.levels))):
      while x.next[i] is not None and x.next[i].val < val:
        x = x.next[i]
      update[i] = x
    return update
  
  def _search(self, val, update = None):
    if update is None:
      update = self._update(val)
    if len(update) > 0:
      node = update[0].next[0]
      if node is not None and node.val == val:
        return node
    return None

  def _insert(self, val: int) -> None:
    # node with val already exist?
    node = self._search(val)
    if node is not None:
      node.count += 1
    else:
      # node creation
      node = Node(val, self._randomLevel())
      # update max level and extend head correspondingly
      self.levels = max(self.levels, len(node.__next__))
      while len(self.head.__next__) < len(node.__next__):
        self.head.next.append(None)
      # update list of candidates
      update = self._update(val)
      for i in range(len(node.__next__)):
        node.next[i] = update[i].next[i]
        update[i].next[i] = node
    return None

  def _delete(self, val: int) -> bool:
    update = self._update(val)
    node = self._search(val, update)
    if node is not None:
      node.count -= 1
      if node.count < 1:
        for i in reversed(list(range(len(node.__next__)))):
          update[i].next[i] = node.next[i]
          if self.head.next[i] is None:
            self.head.next.pop()
            self.levels -= 1
      return True
    else:
      return False

  def display(self) -> None:
    for i in range(len(self.head.__next__) - 1, -1, -1):
      x, s = self.head, ''
      while x.next[i] != None:
        s += str(x.next[i].val) + '(' + str(x.next[i].count) + ') -- '
        x = x.next[i]
      print(('level', '{:4d}'.format(i), ':',  s))

  def search(self, target: int) -> bool:
    return self._search(target) is not None

  def add(self, num: int) -> None:
    return self._insert(num)

  def erase(self, num: int) -> bool:
    return self._delete(num)

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

