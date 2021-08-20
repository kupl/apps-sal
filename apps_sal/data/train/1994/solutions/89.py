class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        temp = head
        count = 0
        c = 0
        if len(G) == 1:
            return 1
        while temp:
            if temp.val in G:
                print(temp.val)
                count += 1
                while temp and temp.val in G:
                    temp = temp.__next__
            else:
                temp = temp.__next__
        return count
