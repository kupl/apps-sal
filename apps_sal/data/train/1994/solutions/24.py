class Solution:

    def numComponents(self, head: ListNode, l: List[int]) -> int:
        l = set(l)
        n = len(l)
        temp = head
        while temp and temp.__next__:
            if temp.val in l and temp.next.val in l:
                n -= 1
            temp = temp.__next__
        return n
