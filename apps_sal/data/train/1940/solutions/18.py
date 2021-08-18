class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head is None:
            return []

        n = 0
        cur = head
        while cur is not None:
            cur = cur.next
            n += 1

        cur = head
        pos = 0
        result = [0] * n
        stack = []

        while cur is not None:
            while stack and stack[-1][0] < cur.val:
                result[stack[-1][1]] = cur.val
                stack.pop()
            stack.append([cur.val, pos])

            cur = cur.next
            pos += 1

        return result
