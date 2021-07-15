# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return None
        queue = []
        queue.append(root)
        result = []
        while len(queue) > 0:
            levellength = len(queue)
            temp = []
            for i in range(levellength):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(temp) > 0:
                result.append(temp)
        return sum(result[-1])
