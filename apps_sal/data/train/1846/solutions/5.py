class Solution:

    def pruneTree(self, root: TreeNode) -> TreeNode:

        def prune_tree_helper(root):
            if root:
                curr_res = True if root.val == 0 else False
                left_res = prune_tree_helper(root.left)
                right_res = prune_tree_helper(root.right)
                if left_res:
                    root.left = None
                if right_res:
                    root.right = None
                return curr_res and left_res and right_res
            else:
                return True
        res = prune_tree_helper(root)
        if res:
            return None
        else:
            return root
