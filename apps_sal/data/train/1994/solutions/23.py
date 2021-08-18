class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        newG = set(G)
        cnt = 0
        start = None
        while head != None:
            if head.val not in newG:
                if start != None:
                    start = None
                    cnt += 1
            else:
                start = 1
            head = head.__next__
        if start != None:
            cnt += 1
        return cnt
