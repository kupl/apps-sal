class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        num_ccs = 0
        nodes = set(G)
        last_was_cc = False
        while head is not None:
            if head.val in nodes:
                if not last_was_cc:
                    num_ccs += 1
                last_was_cc = True
            else:
                last_was_cc = False
            head = head.next
        return num_ccs
