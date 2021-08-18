class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        setG = set(G)
        res = 0
        while head:
            if head.val in setG and (head.__next__ == None or head.next.val not in setG):
                res += 1
            head = head.__next__
        return res
