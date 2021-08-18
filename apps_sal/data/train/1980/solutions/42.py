import random
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None


class Skiplist:
    def __init__(self, levels=30):
        self.heads = [Node(-float('inf')) for _ in range(levels)]
        for c, n in zip(self.heads, self.heads[1:]):
            c.down = n

    def search(self, target) -> bool:
        curr = self.heads[0]
        while curr:
            if curr.next is None or curr.val < target <= curr.next.val:
                if curr.next and target == curr.next.val:
                    return True
                curr = curr.down
            else:
                curr = curr.next
        return False

    def add(self, num: int) -> None:
        stack, curr, pre = deque([]), self.heads[0], None
        while curr:
            if curr.next is None or curr.val < num <= curr.next.val:
                stack.append(curr)
                curr = curr.down
            else:
                curr = curr.next

        while stack:
            curr = stack.pop()
            node = Node(num)
            node.next, curr.next = curr.next, node
            if pre:
                node.down = pre
            pre = node
            if random.randint(0, len(self.heads) - 1) < len(self.heads) - 1:
                break

    def erase(self, num: int) -> bool:
        b, curr = False, self.heads[0]
        while curr:
            if curr.next is None or curr.val < num <= curr.next.val:
                if curr.next and curr.next.val == num:
                    b, curr.next = True, curr.next.next
                curr = curr.down
            else:
                curr = curr.next
        return b
