class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        Gset = set(G)
        current = head
        ans = 0
        while current:
            if current.val in Gset:
                if current.next and current.next.val not in Gset or current.next is None:
                    ans += 1
            current = current.next
        return ans
