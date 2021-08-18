class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:

        comp = False
        count = 0
        while(head):
            if(head.val in G):
                if(not comp):
                    comp = True
            else:
                if(comp):
                    count += 1
                    comp = False

            head = head.next

        return count + 1 if comp else count
