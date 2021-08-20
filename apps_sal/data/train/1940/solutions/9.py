class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head is None:
            return []
        stack = []
        index = 0
        length = 0
        ansarray = [0] * 100001
        while head:
            while len(stack) and head.val > stack[-1][0].val:
                k = stack.pop()
                ansarray[k[1]] = head.val
            stack.append([head, index])
            length += 1
            index += 1
            head = head.next
        return ansarray[:length]
