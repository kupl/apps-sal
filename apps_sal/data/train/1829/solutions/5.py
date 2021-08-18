class Solution:

    def traverse(self, root, currentMax):
        if root != None:
            if currentMax <= root.val:
                self.count += 1
            self.traverse(root.left, max(currentMax, root.val))
            self.traverse(root.right, max(currentMax, root.val))

    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.traverse(root, float('-inf'))
        return self.count
