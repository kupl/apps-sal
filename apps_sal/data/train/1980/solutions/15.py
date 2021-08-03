class Node:
    def __init__(self, val):
        self.val = val
        self.next, self.down = None, None


class Skiplist:

    def __init__(self):
        self.levels = []
        prev = None
        for i in range(16):
            self.levels.append(Node(float('-inf')))
            if prev:
                prev.down = self.levels[-1]
            prev = self.levels[-1]

    def _iter(self, target):
        res = []
        node = self.levels[0]
        while node:
            while node.__next__ and node.next.val < target:
                node = node.__next__
            res.append(node)
            node = node.down
        return res

    def search(self, target: int) -> bool:
        found = self._iter(target)
        return found[-1].__next__ and found[-1].next.val == target

    def add(self, num: int) -> None:
        down = None
        for node in self._iter(num)[::-1]:
            new_node = Node(num)
            new_node.next = node.__next__
            new_node.down = down
            node.next = new_node
            if random.randint(0, 1) == 1:
                return
            down = new_node

    def erase(self, num: int) -> bool:
        found = False
        for node in self._iter(num):
            if node.__next__ and node.next.val == num:
                node.next = node.next.__next__
                found = True

        return found


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
