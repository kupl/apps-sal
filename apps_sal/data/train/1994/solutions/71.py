class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        val = False
        count = 0
        while head:
            if head.val in G:
                val = True

                while head and head.val in G:
                    head = head.__next__
                count += 1
            if head:
                head = head.__next__

        return count
