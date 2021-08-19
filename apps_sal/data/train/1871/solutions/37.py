LEFT_PROCESSED = 1
RIGHT_PROCESSED = 2


class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:

        def recurse_func(node, parent_vals, best_answer):
            if parent_vals:
                ans = abs(min(parent_vals) - node.val)
                if ans > best_answer:
                    best_answer = ans
                ans = abs(max(parent_vals) - node.val)
                if ans > best_answer:
                    best_answer = ans
            parent_vals.append(node.val)
            if node.left:
                best_answer = recurse_func(node.left, parent_vals, best_answer)
            if node.right:
                best_answer = recurse_func(node.right, parent_vals, best_answer)
            parent_vals.pop()
            return best_answer
        return recurse_func(root, [], 0)
