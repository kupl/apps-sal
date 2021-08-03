class Node:
    def __init__(self, val):
        self.val = val
        self.next, self.lower = None, None


class Skiplist:

    def __init__(self):
        self.sentinel = Node(-sys.maxsize)
        self.overhead = Node(-sys.maxsize)
        self.overhead.lower = self.sentinel

    def _flip(self, cur):
        target = None if not cur.__next__ else cur.next.lower
        p, count = cur.lower, 0
        while p != target:
            p = p.__next__
            count += 1
        if count >= 4:
            lower = cur.lower.next.__next__
            new_node = Node(lower.val)
            new_node.next, new_node.lower = cur.__next__, lower
            cur.next = new_node

    def search(self, target: int) -> bool:
        cur = self.sentinel
        while cur:
            if cur.val == target:
                return True
            elif not cur.__next__ or cur.next.val > target:
                cur = cur.lower
            else:
                cur = cur.__next__
        return False

    def add(self, num: int) -> None:
        def insertLower(head):
            cur = head
            while cur.__next__ and cur.next.val <= num:
                cur = cur.__next__
            if cur.lower:
                insertLower(cur.lower)
                self._flip(cur)
            else:
                new_node = Node(num)
                new_node.next = cur.__next__
                cur.next = new_node
        insertLower(self.sentinel)
        count = 0
        p = self.sentinel
        while p:
            p = p.__next__
            count += 1
        if count >= 4:
            new_level = Node(-sys.maxsize)
            lower = self.sentinel.next.__next__
            new_node = Node(lower.val)
            new_node.lower = lower
            new_level.next = new_node
            new_level.lower = self.sentinel
            self.sentinel = new_level

    def erase(self, num: int) -> bool:
        def eraseLower(head):
            cur = head
            while cur.__next__ and cur.next.val < num:
                cur = cur.__next__
            removed = None
            if cur.lower:
                deleted = eraseLower(cur.lower)
                if cur.__next__ and cur.next.lower == deleted:
                    removed = cur.__next__
                    cur.next = cur.next.__next__
                self._flip(cur)
            else:
                removed = cur.__next__
                cur.next = cur.next.__next__
            return removed

        if not self.search(num):
            return False

        eraseLower(self.sentinel)
        while self.sentinel.lower and not self.sentinel.__next__:
            self.sentinel = sentinel.lower
        return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
