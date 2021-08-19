# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        st1 = []
        ptr = head
        while ptr:
            st1.append(ptr.val)
            ptr = ptr.__next__

        st2 = []
        ans = []
        while st1:
            while st2 and st2[-1] <= st1[-1]:
                st2.pop()
            if len(st2) == 0:
                ans.append(0)
            else:
                ans.append(st2[-1])
            st2.append(st1.pop())
        return ans[::-1]
