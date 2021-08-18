class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        cur = head
        cnt = 0
        flg = False
        while cur != None:
            if cur.val in G:
                if flg:
                    pass
                else:
                    flg = True
                    cnt += 1
            elif flg:
                flg = False
            cur = cur.__next__
        return cnt
