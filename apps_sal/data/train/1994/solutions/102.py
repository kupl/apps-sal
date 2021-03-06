class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        res = 0
        curr = head
        found = False
        while curr is not None:
            if not found and curr.val in G:
                found = True
                res += 1
            if found and curr.val not in G:
                found = False
            curr = curr.__next__
        return res
