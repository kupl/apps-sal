class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        if len(G) == 1:
            return 1
        while head:
            if head.val in G:
                print((head.val))
                count += 1
                while head and head.val in G:
                    head = head.__next__
            else:
                head = head.__next__

        return count
