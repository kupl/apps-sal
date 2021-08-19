class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.__next__
        n = len(vals)
        ret = [0 for _ in range(n)]
        q = [(n - 1, vals[n - 1])]
        for i in range(n - 1, -1, -1):
            curr = vals[i]
            while q:
                if q[0][1] > curr:
                    ret[i] = q[0][1]
                    heapq.heappush(q, (i, curr))
                    break
                else:
                    heapq.heappop(q)
            else:
                heapq.heappush(q, (i, curr))
        return ret
