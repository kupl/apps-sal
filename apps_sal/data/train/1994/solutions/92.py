class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        cur = head
        connected = 0

        while cur != None:
            if cur.val in G:
                while cur.val in G:
                    cur = cur.next

                    if cur == None:
                        break

                connected += 1
            else:
                cur = cur.next

        return connected
