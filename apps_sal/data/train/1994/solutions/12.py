class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = len(G)
        temp = head
        while temp.next != None:
            if temp.val in G and temp.next.val in G:
                count -= 1
            temp = temp.next
        return count
