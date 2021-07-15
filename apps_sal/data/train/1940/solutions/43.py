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
                        stack_val = stack.pop()
                        if stack_val[0] < head.val:
                            result[stack_val[1]] = head.val
                        else:
                            stack.append(stack_val)
            stack.append((head.val, index))

            result.append(0)
            index += 1
            head = head.__next__
            
            
        return result
        
            
        

