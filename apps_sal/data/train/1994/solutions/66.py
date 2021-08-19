# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        cur = head
        cnt = 0
        flg = False
        while cur != None:
            if cur.val in G:
                if flg:
                    pass
                else:
                    flg = True
                    cnt += 1
            elif flg:
                flg = False
            cur = cur.__next__
        return cnt
