class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def dfs(onode, cnode, target):
            if onode:
                if onode.val == target.val:
                    return cnode
                else:
                    return dfs(onode.left, cnode.left, target) or dfs(onode.right, cnode.right, target)
        return dfs(original, cloned, target)
