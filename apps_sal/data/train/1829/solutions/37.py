class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def rootToNode(root, path):
            nonlocal count
            if root is None:
                return
            path.append(root.val)
            if max(path) == root.val:
                count += 1
            rootToNode(root.left, path.copy())
            rootToNode(root.right, path.copy())
        rootToNode(root, [])
        return count
