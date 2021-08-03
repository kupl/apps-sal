class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        class Node:
            def __init__(self, val, nextNode=None):
                self.val = val
                self.next = nextNode
        dummy = Node(-1)
        res = {}
        out = []
        cur = dummy

        for i in range(m):
            cur.next = Node(i + 1)
            res[i + 1] = [i, cur.__next__]
            cur = cur.__next__
        cur = dummy
        for query in queries:
            out.append(res[query][0])
            if not res[query][0]:
                continue
            cur = dummy.__next__
            while cur and cur.val != query:
                # print(res[cur.val])
                res[cur.val][0] += 1
                prev = cur
                cur = cur.__next__
            prev.next = cur.__next__
            cur.next = dummy.__next__
            dummy.next = cur
            res[cur.val][0] = 0
        return out
