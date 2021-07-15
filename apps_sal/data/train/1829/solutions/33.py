# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = collections.deque()
        queue.append([root,-float('inf')])
        count = 0
        while queue:
            node, pVal = queue.popleft()
            if node.val >= pVal:
                count += 1
                if node.left:
                    queue.append([node.left, node.val])
                if node.right:
                    queue.append([node.right, node.val])
            else:
                if node.left:
                    queue.append([node.left, pVal])
                if node.right:
                    queue.append([node.right, pVal])
        return count
            

