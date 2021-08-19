class Skiplist:

    class Node:

        def __init__(self, value):
            self.value = value
            self.next = []

    def __init__(self):
        self.max_height = 1
        self.left = self.Node(-float('inf'))
        self.right = self.Node(float('inf'))
        self.left.next.append(self.right)

    def _find(self, target: int) -> bool:
        path = []
        h = len(self.left.__next__) - 1
        pointer = self.left
        while h > -1:
            while pointer.next[h].value < target:
                pointer = pointer.next[h]
            path.append(copy.copy(pointer))
            h -= 1
        return path

    def search(self, target: int) -> bool:
        path = self._find(target)
        return path[-1].next[0].value == target

    def add(self, num: int) -> None:
        path = self._find(num)
        height = 0
        while random.randint(0, 1):
            height += 1
        while height >= len(self.left.__next__):
            self.left.next.append(self.right)
        new = self.Node(num)
        for h in range(height + 1):
            try:
                prev = path[-1 - h]
            except IndexError:
                prev = self.left
            new.next.append(prev.next[h])
            prev.next[h] = new

    def erase(self, num: int) -> bool:
        path = self._find(num)
        node = path[-1].next[0]
        if node.value != num:
            return False
        for (i, x) in enumerate(node.__next__):
            path[-1 - i].next[i] = x
        return True
