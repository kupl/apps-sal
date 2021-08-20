class Solution:

    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if root == None:
            return None

        def dfs(root, val):
            if root == None:
                return (-10000000000.0, 'nodel')
            if root:
                (left_val, left_del_str) = dfs(root.left, val + root.val)
                (right_val, right_del_str) = dfs(root.right, val + root.val)
                if root.left and root.right:
                    cur_val = val + root.val + max(left_val, right_val)
                elif root.left:
                    cur_val = val + root.val + left_val
                elif root.right:
                    cur_val = val + root.val + right_val
                else:
                    cur_val = val + root.val
                if left_del_str == 'del':
                    root.left = None
                if right_del_str == 'del':
                    root.right = None
                if cur_val < limit:
                    return (cur_val - val, 'del')
                else:
                    return (cur_val - val, 'nodel')
        (_, root_del_str) = dfs(root, 0)
        if root_del_str == 'del':
            return None
        else:
            return root
