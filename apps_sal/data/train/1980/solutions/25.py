import random


class Node(object):
    def __init__(self, val):
        self.val = val
        self.cnt = 1
        self.right = None
        self.down = None


class Skiplist:

    def __init__(self):
        self.root = Node(float('-inf'))
        p = self.root
        for _ in range(31):
            p.down = Node(float('-inf'))
            p = p.down
        self.root.right = Node(float('inf'))
        uplevel = self.root
        clevel = self.root.down
        while clevel:
            clevel.right = Node(float('inf'))
            uplevel.right.down = clevel.right
            uplevel = clevel
            clevel = clevel.down

    def search(self, target: int) -> bool:
        p = self.root
        while p:
            if p.val == target:
                return p.cnt > 0
            elif p.right.val <= target:
                p = p.right
            else:
                p = p.down
        return False

    def add(self, num: int) -> None:
        p = self.root
        path = []
        while p:
            if p.val == num:
                while p:
                    p.cnt += 1
                    p = p.down
                return
            elif p.right.val <= num:
                p = p.right
            else:
                path.append(p)
                p = p.down
        node = Node(num)
        node.right = path[-1].right
        path[-1].right = node
        path.pop(-1)
        while path and random.random() < 0.5:
            last_level = path.pop(-1)
            new_node = Node(num)
            new_node.right = last_level.right
            last_level.right = new_node
            new_node.down = node
            node = new_node

    def erase(self, target: int) -> bool:
        p = self.root
        while p:
            if p.val == target:
                if p.cnt > 0:
                    while p:
                        p.cnt -= 1
                        p = p.down
                    return True
                else:
                    return False
            elif p.right.val <= target:
                p = p.right
            else:
                p = p.down
        return False
