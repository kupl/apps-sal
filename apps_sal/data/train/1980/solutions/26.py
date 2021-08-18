class Node:
    def __init__(self, v=None):
        self.val = v
        self.right = None
        self.down = None


class Skiplist:

    def __init__(self, level=16):
        self.level = level
        self.levels = []
        n = None
        for i in range(level):
            node = Node(-float('inf'))
            if self.levels:
                self.levels[-1].down = node
            self.levels.append(node)

    def _iter(self, target):
        n = self.levels[0]
        res = []
        for i in range(self.level):
            while n and n.right and n.val < target and n.right.val < target:
                n = n.right
            res.append(n)
            n = n.down
        return res

    def search(self, target: int) -> bool:
        ns = self._iter(target)
        n = ns[-1]
        return n.right and n.right.val == target

    def add(self, num: int) -> None:
        prev = None
        for n in reversed(self._iter(num)):
            if prev and random.random() < 0.5:
                return
            node = Node(num)
            r = n.right
            n.right = node
            node.right = r
            node.down = prev
            prev = node

    def erase(self, num: int) -> bool:
        for i, n in enumerate(reversed(self._iter(num))):
            if i == 0:
                if not n.right or n.right.val != num:
                    return False
            if n.right:
                n.right = n.right.right
            else:
                break
        return True
