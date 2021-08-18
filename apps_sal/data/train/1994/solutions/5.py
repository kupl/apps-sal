class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        x = []
        count = 0
        while head:
            if head.val in G and (head.__next__ is None or head.next.val not in G):
                count += 1
            head = head.__next__
        return count
