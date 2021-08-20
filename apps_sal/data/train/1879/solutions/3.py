class Solution:

    def deepestLeavesSum(self, root: TreeNode) -> int:
        nxt = [(0, root)]
        tot = 0
        depth = 0
        while nxt:
            (d, cur) = nxt.pop()
            if d == depth:
                tot += cur.val
            elif d > depth:
                tot = cur.val
                depth = d
            nxt.extend([(d + 1, x) for x in [cur.left, cur.right] if x])
        return tot
