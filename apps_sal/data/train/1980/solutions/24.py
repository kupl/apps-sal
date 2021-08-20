import random


class Node:

    def __init__(self, val, level, count=1):
        self.val = val
        self.next = [None] * (level + 1)
        self.count = count


class Skiplist:

    def __init__(self, p=0.5):
        self.p = p
        self.head = Node(None, 0)
        self.levels = 1

    def _randomLevel(self):
        _level = 0
        while random.random() < self.p:
            _level += 1
        return _level

    def _update(self, val):
        update = [None] * self.levels
        x = self.head
        for i in reversed(range(self.levels)):
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

    def _insert(self, val: int) -> None:
        node = self._search(val)
        if node is not None:
            node.count += 1
        else:
            node = Node(val, self._randomLevel())
            self.levels = max(self.levels, len(node.next))
            while len(self.head.next) < len(node.next):
                self.head.next.append(None)
            update = self._update(val)
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
        return None

    def _delete(self, val: int) -> bool:
        update = self._update(val)
        node = self._search(val, update)
        if node is not None:
            node.count -= 1
            if node.count < 1:
                for i in reversed(range(len(node.next))):
                    update[i].next[i] = node.next[i]
                    if self.head.next[i] is None:
                        self.head.next.pop()
                        self.levels -= 1
            return True
        else:
            return False

    def display(self) -> None:
        for i in range(len(self.head.next) - 1, -1, -1):
            (x, s) = (self.head, '')
            while x.next[i] != None:
                s += str(x.next[i].val) + '(' + str(x.next[i].count) + ') -- '
                x = x.next[i]
            print('level', '{:4d}'.format(i), ':', s)

    def search(self, target: int) -> bool:
        return self._search(target) is not None

    def add(self, num: int) -> None:
        return self._insert(num)

    def erase(self, num: int) -> bool:
        return self._delete(num)


def __starting_point():
    skiplist = Skiplist()
    skiplist.add(1)
    skiplist.add(2)
    skiplist.add(3)
    print(skiplist.search(0))
    skiplist.add(4)
    skiplist.add(2)
    print(skiplist.display())
    print(skiplist.search(1))
    skiplist.erase(0)
    skiplist.erase(1)
    print(skiplist.search(1))
    skiplist.erase(2)
    print(skiplist.search(2))
    print(skiplist.display())


__starting_point()
