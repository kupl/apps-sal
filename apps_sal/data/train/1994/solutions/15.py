class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        temp = head
        while temp:
            if temp.val in G and (temp.__next__ == None or temp.next.val not in G):
                count += 1
            temp = temp.__next__
        return count
