class Node:
    __slots__ = 'val', 'levels'

    def __init__(self, val, levels):
        self.val = val
        self.levels = [None] * levels


class Skiplist(object):
    def __init__(self):
        self.head = Node(-1, 16)

    def _iter(self, num):
        cur = self.head
        for level in range(15, -1, -1):
            while True:
                nxt = cur.levels[level]
                if nxt and nxt.val < num:
                    cur = nxt
                else:
                    break
            yield cur, level

    def search(self, target):
        for prev, level in self._iter(target):
            pass
        cur = prev.levels[0]
        return cur and cur.val == target

    def add(self, num):
        nodelvls = random.randint(1, 16)
        node = Node(num, nodelvls)
        for cur, level in self._iter(num):
            if level >= nodelvls:
                continue
            future = cur.levels[level]
            cur.levels[level] = node
            node.levels[level] = future

    def erase(self, num):
        ans = False
        for cur, level in self._iter(num):
            nxt = cur.levels[level]
            if nxt and nxt.val == num:
                ans = True
                cur.levels[level] = nxt.levels[level]
        return ans

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
