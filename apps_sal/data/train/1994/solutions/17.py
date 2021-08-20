class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        while head:
            if head.val in G and (head.next == None or head.next.val not in G):
                count += 1
            head = head.next
        return count
