# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        result = [0]
        stack = list()
        position = 0
        while head:
            while len(stack) and stack[-1][0] < head.val:
                result[stack[-1][1]] = head.val
                stack.pop()
            if len(result) <= position:
                result += [0] * (position - len(result) + 1)
            stack.append((head.val, position))
            position += 1
            head = head.next

        return result
