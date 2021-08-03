# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        # Walk the tree

        def recurse_func(node, parent_vals, best_answer):
            # check if we can compute a better answer with this node
            for x in parent_vals:
                ans = abs(x - node.val)
                if ans > best_answer:
                    best_answer = ans

            # check our children
            # there is some optimization that can occur here to prune entire branches if we detect the best answer is larger
            # than the largest value we expect to find in the tree branch, but we would need to record whether we came down the left or right branch of the parent
            parent_vals.append(node.val)
            if node.left:
                best_answer = recurse_func(node.left, parent_vals, best_answer)
            if node.right:
                best_answer = recurse_func(node.right, parent_vals, best_answer)
            parent_vals.pop()

            # return best_answer
            return best_answer

        return recurse_func(root, [], 0)
