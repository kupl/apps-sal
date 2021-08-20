class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 1
        (parents, children) = ([(root, root.val)], [])
        while parents:
            for (node, val) in parents:
                if node.left:
                    if node.left.val >= val:
                        res += 1
                    children.append((node.left, max(val, node.left.val)))
                if node.right:
                    if node.right.val >= val:
                        res += 1
                    children.append((node.right, max(val, node.right.val)))
            parents = children
            children = []
        return res
