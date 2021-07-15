# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        answer = []
        index = 0
        while head:
            answer.append(0)
            while len(stack) > 0 and stack[-1][0] < head.val:
                number_and_index = stack.pop()                
                answer[number_and_index[1]] = head.val
            stack.append((head.val, index))
            index += 1
            head = head.next
        return answer
