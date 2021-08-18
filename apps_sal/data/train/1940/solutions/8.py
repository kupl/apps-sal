class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return []
        orig_head = head
        all_res = []
        stack = []
        i = 0
        while head:
            while stack:
                v, j = stack[-1]
                if head.val > v:
                    all_res.append((head.val, j))
                    stack.pop()
                else:
                    break
            stack.append((head.val, i))
            head = head.__next__
            i += 1
        while stack:
            _, top = stack.pop()
            all_res.append((0, top))
        all_res = sorted(all_res, key=lambda x: x[1])
        return [v for v, _ in all_res]
