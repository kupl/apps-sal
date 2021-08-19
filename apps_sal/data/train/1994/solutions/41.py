# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        if not head or not G:
            return 0
        allCom = []
        com = []
        while head:

            while head and head.val in G:
                com.append(head.val)
                G.remove(head.val)
                head = head.__next__
            # constructed component?
            if com:
                allCom.append(com)
                com = []
            if head:
                head = head.__next__
            else:
                break
        return len(allCom)
