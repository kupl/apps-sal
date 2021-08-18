class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        temp = head
        while temp:
            if temp.val not in G:
                temp = temp.__next__
                continue
            curr = temp.__next__
            while curr:
                if curr.val not in G:
                    curr = curr.__next__
                    break
                else:
                    curr = curr.__next__
            count += 1
            temp = curr
        return count
