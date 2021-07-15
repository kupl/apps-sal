# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        nodes = []
        curr = head
        while curr: 
            nodes.append(curr.val)
            curr = curr.next
        res = [0]*len(nodes)
        stack = []
        
        for i in range(len(nodes)): 
            while stack and nodes[stack[-1]]<nodes[i]: 
                res[stack.pop()] = nodes[i]
            
            stack.append(i)
        
        return res
