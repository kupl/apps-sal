class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        traverse_count = 0

        def traverse(node, max_val=float('-inf')):
            nonlocal traverse_count
            if not node:
                return
            if node.val >= max_val:
                traverse_count += 1
            max_val = max(max_val, node.val)
            traverse(node.left, max_val)
            traverse(node.right, max_val)
        traverse(root)
        return traverse_count
