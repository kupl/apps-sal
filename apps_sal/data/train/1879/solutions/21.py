

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [root]
        while True:
            q_new = [x.left for x in q if x.left]
            q_new += [x.right for x in q if x.right]
            if not q_new:
                break
            q = q_new
        return sum([node.val for node in q])
