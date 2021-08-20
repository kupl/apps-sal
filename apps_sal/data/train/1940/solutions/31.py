class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = []
        i = 0
        prev_min = sys.maxsize
        val = set()
        curr = head
        while curr != None:
            n = curr.val
            if n > prev_min:
                to_remove = []
                for node in val:
                    if node[1] < n:
                        res[node[0]] = n
                        to_remove.append(node)
                for node in to_remove:
                    val.remove(node)
            else:
                prev_min = n
            val.add((i, n))
            res.append(0)
            curr = curr.__next__
            i += 1
        return res
