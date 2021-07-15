# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        return self.stacksol(head)
        \"\"\"
        1) Go backwards
        2) Keep sorted list of numbers
        3) Upon new number, insert into list in sorted order, and remove all values smaller than that number
            a) if new number is at the end of the list (max), then return 0 for that value
            b) else, return the next larger value in the list
        \"\"\"
        vals = [] #list form of linked list
        while(head):
            vals += [head.val]
            head = head.next
        
        slist = [] #sorted max list
        alist = [] #answer
        
        for i,val in enumerate(vals[::-1]):
            newind = bisect.bisect_right(slist, val)
            slist.insert(newind, val)
            if slist[-1] == val:
                alist += [0]
            else:
                alist += [slist[newind+1]]
            slist = slist[newind:]
            
        return alist[::-1]
    
    def stacksol(self, head: ListNode) -> List[int]:
        \"\"\"
        add numbers to stack
        1) pop off all numbers lower than number first
        2) add number to answer list, in equal number of pops (else add 0 place holder)
        3) 
        
        \"\"\"
        ret, stack = [], []
        
        while(head):
            while(stack and stack[-1][0] < head.val):
                p = stack.pop()
                ret[p[1]] = head.val
            stack += [(head.val, len(ret) )]

            ret += [0]
            head = head.next
        return ret
    
    
#         ret, stack = [], []
#         while(head):
#             counter = 0
#             while(stack and stack[-1] < head.val):
#                 stack.pop()
#                 counter += 1
#             stack += [head.val]

#             for i in range(counter):
#                 ret[-(i+1)] = head.val
#             ret += [0]
#             head = head.next
#         return ret
