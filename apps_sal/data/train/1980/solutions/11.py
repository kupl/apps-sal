import math
import random


class Node:

    def __init__(self, val):
        self.next = None
        self.prev = None
        self.down = None
        self.val = val


class Skiplist:

    def __init__(self):
        self.lvls = math.ceil(math.log(50000) / math.log(2))
        self.topleft = self.add_first(-1 << 31)

    def search_(self, target: int):
        x = self.topleft
        out = []
        while True:
            while x.__next__ and x.next.val <= target:
                x = x.__next__
            out.append(x)
            if x.down:
                x = x.down
            else:
                break
        return out

    def ll_to_list(self, x):
        out = []
        while x:
            out.append(x.val)
            x = x.__next__
        return out

    def print_lvls(self):
        x = self.topleft
        for i in range(self.lvls):
            print(self.ll_to_list(x))
            x = x.down
        print()

    def search(self, target: int) -> bool:
        x = self.topleft
        while True:
            while x.__next__ and x.next.val <= target:
                x = x.__next__
            if x.down:
                x = x.down
            else:
                break
        if x and x.val == target:
            return True
        return False

    def insert(self, x, num):
        n = Node(num)
        (p, q) = (x, x.__next__)
        p.next = n
        n.prev = p
        n.next = q
        if q:
            q.prev = n
        return n

    def add_first(self, num):
        prev = None
        for i in range(self.lvls - 1, -1, -1):
            n = Node(num)
            if prev:
                n.down = prev
            prev = n
        return prev

    def add(self, num: int) -> None:
        xs = self.search_(num)
        prev = self.insert(xs[self.lvls - 1], num)
        for i in range(self.lvls - 2, -1, -1):
            if random.random() > 0.5:
                curr = self.insert(xs[i], num)
                if prev:
                    curr.down = prev
                prev = curr
            else:
                break

    def delete(self, x):
        (p, q, r) = (x.prev, x, x.__next__)
        p.next = r
        if r:
            r.prev = p

    def erase(self, num: int) -> bool:
        xs = self.search_(num)
        prev = None
        found = False
        for i in range(self.lvls - 1, -1, -1):
            if xs[i].val == num:
                found = True
                self.delete(xs[i])
            else:
                break
        return found
