class Node:
    def __init__(self, val, lev, count=1):
        self.val = val
        self.next = [None] * lev
        self.count = count


class Skiplist:

    def __init__(self, p=0.5):
        self.p = p
        self.head = Node(None, 1)
        self.levels = 1

    def _random_level(self):
        _level = 1
        while random.random() < self.p:
            _level += 1
        return _level

    def _update(self, val):
        update = [None] * self.levels
        x = self.head
        for i in reversed(list(range(self.levels))):
            while x.next[i] is not None and x.next[i].val < val:
                x = x.next[i]
            update[i] = x
        return update

    def _search(self, val, update=None):
        if update is None:
            update = self._update(val)
        if len(update) > 0:
            node = update[0].next[0]
        if node is not None and node.val == val:
            return node
        return None

    def _insert(self, val):
        node = self._search(val)
        if node is not None:
            node.count += 1
        else:
            node = Node(val, self._random_level())
            self.levels = max(self.levels, len(node.__next__))
            while len(self.head.__next__) < len(node.__next__):
                self.head.next.append(None)
            update = self._update(val)
            for i in range(len(node.__next__)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
        return None

    def _delete(self, val):
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
