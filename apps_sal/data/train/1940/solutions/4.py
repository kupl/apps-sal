class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head is None:
            return []
        if head.next is None:
            return [0]

        i = head
        stack = []
        out = []
        count = 0
        while i:
            if not stack:
                stack.append([count, i.val])
            elif i.val <= stack[-1][1]:
                stack.append([count, i.val])
            else:
                while stack and i.val > stack[-1][1]:
                    tmp_count, tmp_val = stack.pop()
                    out.append([tmp_count, i.val])
                stack.append([count, i.val])
            i = i.next
            count += 1

        output = [0] * count
        for i, j in out:
            output[i] = j
        return output
