class Node:

    def __init__(self, val, next=None, down=None):
        self.val = val
        self.next = next
        self.down = down


class Skiplist:
    import random

    def __init__(self):
        self.heads = []
        self.level = 0

    def printList(self):
        res = []
        for head in self.heads:
            (curr, l) = (head.__next__, [])
            while curr:
                l.append(curr.val)
                curr = curr.__next__
            res.append(l)
        return res

    def search(self, target: int) -> bool:
        curr = self.heads[-1]
        while curr:
            while curr.__next__ and curr.next.val < target:
                curr = curr.__next__
            if curr.__next__ and curr.next.val == target:
                return True
            curr = curr.down
        return False

    def add(self, num: int) -> None:
        if not self.heads:
            head = Node(-1, Node(num, None, None), None)
            self.heads.append(head)
            self.level = 1
            return
        newLevel = 1
        while newLevel <= self.level and (not random.randint(1, 100) & 1):
            newLevel += 1
        addNewLevel = False
        if newLevel > self.level:
            self.level = newLevel
            node = Node(num, None, None)
            head = Node(-1, node, self.heads[-1]) if self.heads else Node(-1, node, None)
            self.heads.append(head)
            addNewLevel = True
        if addNewLevel:
            if len(self.heads) == 1:
                return
            (curr, prev) = (self.heads[-2], self.heads[-1].__next__)
        else:
            (curr, prev) = (self.heads[-1], None)
        for i in range(self.level - 1 if addNewLevel else self.level, 0, -1):
            while curr.__next__ and curr.next.val < num:
                curr = curr.__next__
            if i <= newLevel:
                curr.next = Node(num, curr.next, None)
                if prev:
                    prev.down = curr.__next__
                prev = curr.__next__
            curr = curr.down

    def erase(self, num: int) -> bool:
        curr = self.heads[-1]
        seen = False
        for i in range(self.level):
            while curr.__next__ and curr.next.val < num:
                curr = curr.__next__
            if curr.__next__ and curr.next.val == num:
                seen = True
                tmp = curr.__next__
                curr.next = curr.next.__next__
                tmp = None
            curr = curr.down
        return seen
