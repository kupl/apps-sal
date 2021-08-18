class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:

        if not root or not root.left and not root.right:
            return 0
        self.max_val = 0
        self.traverseWithAncestor(root, [])

        return self.max_val

    def traverseWithAncestor(self, root, ancestors):

        if not root:
            return

        for v in ancestors:
            if (res := abs(root.val - v)) > self.max_val:
                self.max_val = res

        if not root.left and not root.right:
            return

        newAncestors = list(ancestors)
        newAncestors.append(root.val)
        if root.left:
            self.traverseWithAncestor(root.left, newAncestors)
        if root.right:
            self.traverseWithAncestor(root.right, newAncestors)
