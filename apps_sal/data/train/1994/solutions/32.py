class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        c = 0
        els = {}
        check = False
        for el in G:
            els[el] = True
        while head != None:
            if head.val in els:
                if not check:
                    c += 1
                    check = True
            else:
                check = False
            head = head.__next__
        return c
