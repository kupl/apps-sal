class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        Gset = set(G)
        cur = head
        noOfcomponents = 0
        while cur:
            if cur.val in Gset and (not cur.__next__ or cur.next.val not in Gset):
                noOfcomponents += 1
                cur = cur.__next__
            else:
                cur = cur.__next__
        return noOfcomponents
