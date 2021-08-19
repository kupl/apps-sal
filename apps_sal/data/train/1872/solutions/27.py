class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        q = [root]
        curr_level = 1
        max_level = 1
        max_sum = root.val
        while len(q) != 0:
            level_nodes = len(q)
            sum_ = 0
            for i in range(level_nodes):
                root = q[0]
                if root != None:
                    sum_ += root.val
                if root.left != None:
                    q.append(root.left)
                if root.right != None:
                    q.append(root.right)
                del q[0]
            if sum_ > max_sum:
                max_sum = sum_
                max_level = curr_level
            curr_level += 1
        return max_level
