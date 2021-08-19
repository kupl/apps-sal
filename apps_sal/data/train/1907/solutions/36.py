class Solution:
    find = None
    target = None

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.target = target
        self.dfs(cloned)
        return self.find

    def dfs(self, tree: TreeNode):
        if not tree:
            return
        if tree.val == self.target.val:
            if tree.left and tree.right:
                if tree.left.val == self.target.left.val and tree.right.val == self.target.right.val:
                    self.find = tree
                    return
            if tree.left:
                if tree.left.val == self.target.left.val and (not tree.right) and (not self.target.right):
                    self.find = tree
                    return
            if tree.right:
                if tree.right.val == self.target.right.val and (not tree.left) and (not self.target.left):
                    self.find = tree
                    return
            if not tree.left and (not tree.right):
                if not self.target.left and (not self.target.right):
                    self.find = tree
                    return
        if tree.left:
            self.dfs(tree.left)
        if tree.right:
            self.dfs(tree.right)
