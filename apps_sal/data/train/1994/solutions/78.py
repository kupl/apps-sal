class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        p = head
        while(p != None):
            if p.val in G:
                count += 1
                q = p.next
                while(q != None and q.val in G):
                    q = q.next
                p = q
            else:
                p = p.next

        return count
