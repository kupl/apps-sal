class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        res = [0]
        tmp_count = 0
        while head:
            if head.val not in G:
                res.append(tmp_count)
                tmp_count = 0
            else:
                tmp_count += 1

            head = head.__next__
        res.append(tmp_count)
        count = 0
        for i in res:
            if i != 0:
                count += 1
        return count
