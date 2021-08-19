class Solution:

    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return False
        stack = [(root, [])]
        res = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
        while stack:
            (curr_node, path) = stack.pop()
            if not curr_node.left and (not curr_node.right):
                path.append(chr(97 + curr_node.val))
                path_rev = reversed(path)
                p = ''.join(path_rev)
                res = min(res, p)
            if curr_node.left:
                path1 = path.copy()
                path1.append(chr(97 + curr_node.val))
                stack.append((curr_node.left, path1))
            if curr_node.right:
                path1 = path.copy()
                path1.append(chr(97 + curr_node.val))
                stack.append((curr_node.right, path1))
        return res
