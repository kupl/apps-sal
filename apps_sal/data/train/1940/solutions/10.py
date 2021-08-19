class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        p = head
        stack = []
        d = collections.defaultdict(deque)
        res = []
        length = 0
        while p:
            while stack and stack[-1] < p.val:
                val = stack.pop()
                d[val].append(p.val)
            stack.append(p.val)
            p = p.__next__
            length += 1
        while head:
            if head.val in d:
                if d[head.val]:
                    res.append(d[head.val].popleft())
                else:
                    res.append(0)
            else:
                res.append(0)
            head = head.__next__
        return res
