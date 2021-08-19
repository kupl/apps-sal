# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:

        st = []
        ret = []

        def get_nxt_grt(cur):
            if not cur:
                return

            get_nxt_grt(cur.__next__)

            while st and st[-1] <= cur.val:
                st.pop()

            if not st:
                ret.append(0)
            else:
                ret.append(st[-1])
            st.append(cur.val)

        get_nxt_grt(head)
        return ret[::-1]
