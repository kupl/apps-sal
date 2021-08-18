class Solution:
    def numComponents_v1(self, head: ListNode, G: List[int]) -> int:

        count = 0
        new_comp = False
        while head:

            if head.val in G:
                if not new_comp:
                    new_comp = True
                    count += 1
            else:
                new_comp = False

            head = head.__next__

        return count

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        return self.numComponents_v1(head, G)
