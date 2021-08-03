# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:

        temp = head
        inG = {}

        N = 1
        inG[temp.val] = None
        while(temp.__next__ != None):
            inG[temp.next.val] = None
            temp = temp.__next__
            N += 1

        for g in G:
            inG[g] = g

        temp = head
        while(temp.__next__ != None):
            if(inG[temp.next.val] != None and inG[temp.val] != None):
                # connect temp and temp.next in G list
                inG[temp.next.val] = inG[temp.val]

            temp = temp.__next__

        if(None not in set(inG.values())):
            return 1
        else:
            return len(set(inG.values())) - 1
