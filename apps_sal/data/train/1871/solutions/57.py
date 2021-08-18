class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        stack = [[root, [root.val]]]
        res = 0
        while stack:
            node, ancestors = stack[0]
            res = max(res, abs(node.val - ancestors[0]), abs(node.val - ancestors[-1]))
            for i in range(len(ancestors)):
                if node.val >= ancestors[i]:
                    new_ancestors = ancestors[0:i] + [node.val] + ancestors[i:]
                    break
                if i == len(ancestors) - 1:
                    new_ancestors = ancestors + [node.val]
            if node.left != None:
                stack.append([node.left, new_ancestors])
            if node.right != None:
                stack.append([node.right, new_ancestors])
            stack = stack[1:]
        return(res)
