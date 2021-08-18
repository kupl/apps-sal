class SkipNode:
    def __init__(self, val=None, height=0):
        self.val = val
        self.count = 1
        self.next = [None] * height


class Skiplist:

    def __init__(self):
        self.head = SkipNode()
        self.height = 0

    def get_path(self, val):
        path = [None] * self.height
        current = self.head
        for index in reversed(list(range(self.height))):
            while current.next[index] is not None and current.next[index].val < val:
                current = current.next[index]
            path[index] = current
        return path

    def find(self, val, path=None):
        if path is None:
            path = self.get_path(val)
        if path:
            match = path[0].next[0]
            if match and match.val == val:
                return match
        return None

    def get_height(self):
        height = 1
        while randint(0, 1) and height <= (2 * self.height) + 1:
            height += 1
        return height

    def search(self, target: int) -> bool:
        path = self.get_path(target)
        node = self.find(target, path)
        return node is not None and node.val == target

    def add(self, num: int) -> None:
        new_node = SkipNode(num, self.get_height())
        self.height = max(self.height, len(new_node.__next__))
        while len(self.head.__next__) < len(new_node.__next__):
            self.head.next.append(None)
        path = self.get_path(num)
        node = self.find(num, path)
        if node is None:
            for i in range(len(new_node.__next__)):
                new_node.next[i], path[i].next[i] = path[i].next[i], new_node
        else:
            node.count += 1

    def erase(self, num: int) -> bool:
        path = self.get_path(num)
        node = self.find(num, path)
        if not node:
            return False

        if node.count == 1:
            for i in range(len(node.__next__) - 1, -1, -1):
                path[i].next[i] = node.next[i]
                if self.head.next[i] == None:
                    self.height -= 1
        else:
            node.count -= 1
        return True
