class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        res = 0
        flag = 0
        while head:
            if head.val in G:
                if flag == 0:
                    res += 1
                flag = 1
            else:
                flag = 0
            head = head.next
        return res
