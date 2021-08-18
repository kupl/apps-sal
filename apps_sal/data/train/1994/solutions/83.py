class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        temp = head
        count = 0
        while temp:
            if temp.val in G:
                while temp and temp.val in G:
                    temp = temp.next
                count += 1
                if not temp:
                    break
            temp = temp.next
        return count
