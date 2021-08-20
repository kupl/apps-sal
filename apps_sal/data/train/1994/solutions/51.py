class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        if not head or not G:
            return 0
        count = 0
        flag = 0
        while head:
            if head.val in G:
                flag = 1
            elif flag:
                count += 1
                flag = 0
            head = head.next
        if flag:
            count += 1
        return count
