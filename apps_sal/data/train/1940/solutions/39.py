# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        
    
        stack = []
        result = []
        index = 0
        while(head):
            
            if len(stack) > 0:
                if head.val > stack[-1][0]:
                    # Pop the stack, change the list
                    for i in range(len(stack)):
                        if stack[-1][0] < head.val:
                            result[stack.pop()[1]] = head.val
                    
            stack.append((head.val, index))

            result.append(0)
            index += 1
            head = head.__next__
            
            
        return result
        
            
        

