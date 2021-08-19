class Node:
    def __init__(self, val, next=None, down=None):
        self.val = val
        self.next = next
        self.down = down


class Skiplist:
    # https://www.youtube.com/watch?v=1kF6W_9QNp8
    import random

    def __init__(self):
        self.heads = []
        self.level = 0

    def printList(self):
        res = []
        for head in self.heads:
            curr, l = head.__next__, []
            while curr:
                l.append(curr.val)
                curr = curr.__next__
            res.append(l)
        return res

    def search(self, target: int) -> bool:
        # print('search {0}'.format(target))
        curr = self.heads[-1]
        while curr:
            while curr.__next__ and curr.next.val < target:
                curr = curr.__next__
            # print('curr = {0}'.format(curr.val if curr else -1))
            if curr.__next__ and curr.next.val == target:
                return True
            curr = curr.down
        return False

    def add(self, num: int) -> None:
        # print('add {0}'.format(num))
        if not self.heads:
            head = Node(-1, Node(num, None, None), None)
            self.heads.append(head)
            self.level = 1
            # print('list = {0}'.format(self.printList()))
            return
        newLevel = 1
        while newLevel <= self.level and not random.randint(1, 100) & 1:
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
            curr, prev = self.heads[-2], self.heads[-1].__next__
        else:
            curr, prev = self.heads[-1], None
        # print('addNewLevel = {0}, curr = {1}, level = {2}, heads size = {3}, prev = {4}'.format(addNewLevel, curr.val, self.level, len(self.heads), -1 if not prev else prev.val))
        # print('newLevel = {0}'.format(newLevel))
        for i in range(self.level - 1 if addNewLevel else self.level, 0, -1):
            while curr.__next__ and curr.next.val < num:
                curr = curr.__next__
            if i <= newLevel:
                curr.next = Node(num, curr.next, None)
                if prev:
                    prev.down = curr.__next__
                prev = curr.__next__
            curr = curr.down
        # print('list = {0}'.format(self.printList()))

    def erase(self, num: int) -> bool:
        # print('erase {0}'.format(num))
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
        # print('erase {0}, list = {1}'.format(num, self.printList()))
        return seen


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
