# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        ######################################################################
       # solution 1, using stack
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.__next__

        result = [0] * len(stack)  # populate
        stack2 = []

        for i in range(len(stack)):
            while stack2 and stack[stack2[-1]] < stack[i]:
                result[stack2.pop()] = stack[i]
            stack2.append(i)

        while stack2:  # reaplce the indexes of the stack with 0s
            result[stack2.pop()] = 0

        return result
    ######################################################################
        # solution 2, using stack with two for loops
#         output = []
#         if head.next == None:
#             return output + [0]
#         curr = head
#         stack = []
#         while curr:
#             stack.append(curr.val)
#             curr = curr.next

#         for i in range(len(stack)-1):
#             flag = True
#             for j in range(i, len(stack)):
#                 if stack[i] < stack[j]:
#                     output.append(stack[j])
#                     flag = False
#                     break
#             if flag:
#                 output.append(0)
#         return output + [0]
        ######################################################################
