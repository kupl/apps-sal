class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        initial_c = len(G)
        runner = head
        count = 0
        while runner:
            if runner.val in G and getattr(runner.next, 'val', None) not in G:
                count += 1
            runner = runner.next
        return count
