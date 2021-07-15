# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head):
        \"\"\"
        :type head: ListNode
        :rtype: List[int]
        \"\"\"
        answer_array = []
        stack = []
        index = 0
        
        while head is not None:
            answer_array.append(0)
            current_value = head.val
            
            while stack and stack[-1][0] < current_value:
                last_value = stack.pop()
                answer_array[last_value[1]] = current_value

            stack.append((current_value, index))
            index += 1
            head = head.next

        return answer_array
            
        

