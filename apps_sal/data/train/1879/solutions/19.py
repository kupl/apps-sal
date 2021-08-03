class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = deque([root])
        last_t = 0
        while queue:
            l_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                l_sum += node.val

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            l_sum, last_t = 0, l_sum

        return last_t
