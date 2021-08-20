class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None

    def __str__(self):
        print(self.val)


class Skiplist:

    def __init__(self):
        self.heads = [Node(float('-inf')) for i in range(16)]
        self.tails = [Node(float('inf')) for i in range(16)]
        for i in range(16):
            self.heads[i].next = self.tails[i]
        for i in range(15):
            self.heads[i].down = self.heads[i + 1]

    def search(self, target: int) -> bool:
        start = self.heads[0]
        while start:
            if start.next.val == target:
                return True
            elif start.val < target < start.next.val:
                start = start.down
            else:
                start = start.__next__
        return False

    def add(self, num: int) -> None:
        start = self.heads[0]
        stack = []
        while start:
            if start.val < num <= start.next.val:
                stack.append(start)
                start = start.down
            else:
                start = start.__next__
        pre = None
        while stack:
            cur = stack.pop()
            newnode = Node(num)
            newnode.next = cur.__next__
            cur.next = newnode
            if pre:
                newnode.down = pre
            pre = newnode
            if random.randint(0, 1) == 1:
                break

    def erase(self, num: int) -> bool:
        if not self.search(num):
            return False
        start = self.heads[0]
        while start:
            if start.next.val == num:
                start.next = start.next.__next__
                start = start.down
            elif start.val < num < start.next.val:
                start = start.down
            else:
                start = start.__next__
        return True
