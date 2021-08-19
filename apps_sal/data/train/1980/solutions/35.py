class Node:
    def __init__(self, v, i):
        self.v = (v, i)
        self.next = None


class Skiplist:
    def __init__(self):
        self.Levels = []
        self.Levels.append(Node(-1, -1))
        self.Levels[0].next = Node(10000000, 10000000)
        self.Hash = {(-1, -1): [self.Levels[0]]}

    def search(self, target: int) -> bool:
        # print('search',target)
        # for l in self.Levels:
        #     print('new level')
        #     while l:
        #         print(l.v)
        #         l = l.next
        height = len(self.Levels) - 1
        start = self.Levels[-1]
        old = self.Levels[-1]
        while height >= 0:
            start = self.Hash[old.v][height]
            while start.v[0] <= target:
                old = start
                new = start.__next__
                start = start.__next__
            if old.v[0] == target:
                return True
            height -= 1
        return False

    def add(self, num: int) -> None:
        # print('add',num)
        cand = []
        height = len(self.Levels) - 1
        # start = self.Levels[-1]
        # start = self.Hash[old.v][height]
        old = self.Levels[-1]
        while height >= 0:
            start = self.Hash[old.v][height]
            while start.v[0] <= num:
                old = start
                new = start.__next__
                start = start.__next__
            cand.append(old)
            height -= 1
        # print(cand)
        i, flag = len(cand) - 1, True
        new = (num, cand[-1].v[1] + 1) if cand[-1].v[0] == num else (num, 0)
        self.Hash[new] = []
        while flag:
            node = Node(new[0], new[1])
            self.Hash[new].append(node)
            if i >= 0:
                left, right = cand[i], cand[i].__next__
                left.next = node
                node.next = right
                i -= 1
            else:
                t = Node(-1, -1)
                self.Hash[(-1, -1)].append(t)
                self.Levels.append(t)
                self.Levels[-1].next = node
                node.next = Node(10000000, 10000000)
            flag = random.choices([True, False], [0.5, 0.5])[0]
        # for l in self.Levels:
        #     print('new level')
        #     while l:
        #         print(l.v)
        #         l = l.next

    def erase(self, num: int) -> bool:
        # print('erase',num)
        cand = []
        height = len(self.Levels) - 1
        old = self.Levels[-1]
        while height >= 0:
            start = self.Hash[old.v][height]
            while start.v[0] < num:
                old = start
                new = start.__next__
                start = start.__next__
            cand.append(old)
            height -= 1
        todel = cand[-1].__next__
        if todel.v[0] != num:
            return False
        l = len(cand)
        # for c in cand:
        #     print(c.v)
        for i in range(l - 1, -1, -1):
            if cand[i].next.v == todel.v:
                t = cand[i].__next__
                cand[i].next = t.__next__
                t.next = None
            else:
                break
        del self.Hash[todel.v]
        # for l in self.Levels:
        #     print('new level')
        #     while l:
        #         print(l.v)
        #         l = l.next
        return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
