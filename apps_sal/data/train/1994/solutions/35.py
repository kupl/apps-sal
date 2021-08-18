class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        if head == None:
            return 0
        if len(G) == 0:
            return 0

        resNum = 0
        pre = None
        GG = set(G)
        while head:
            if head.val in GG and resNum == 0:
                resNum += 1
            elif head.val in GG and pre not in GG:
                resNum += 1

            pre = head.val
            head = head.next

        return resNum
