class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        visited = set()

        def countNode(node: TreeNode, maxVal: int) -> int:
            if not node:
                return 0
            if node.val >= maxVal:
                return 1 + countNode(node.left, node.val) + countNode(node.right, node.val)
            else:
                return 0 + countNode(node.left, maxVal) + countNode(node.right, maxVal)
        return countNode(root, root.val)
