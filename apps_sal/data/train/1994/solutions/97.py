class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        counter = 0
        prev, current = None, head

        while current:
            if current.val in G:
                if not prev or prev.val not in G:
                    counter += 1

            prev, current = current, current.__next__

        return counter
