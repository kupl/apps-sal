class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.__next__
        result = [0] * len(stack)
        stack2 = []
        for i in range(len(stack)):
            while stack2 and stack[stack2[-1]] < stack[i]:
                result[stack2.pop()] = stack[i]
            stack2.append(i)
        while stack2:
            result[stack2.pop()] = 0
        return result
