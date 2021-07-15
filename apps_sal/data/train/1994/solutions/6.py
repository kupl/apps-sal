# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        
        
        flag=0
        count=0
        temp=head
        while temp:
            if temp.val in G:
                flag=1
            else:
                if flag == 1:
                    count+=1
                    
                flag=0
                
            temp=temp.next
            
        if flag==1:
            count+=1
            
        return count
