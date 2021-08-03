# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
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
