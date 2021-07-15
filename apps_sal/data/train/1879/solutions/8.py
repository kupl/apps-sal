# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        s = 0
        q = deque()
        temp = deque()
        if root == None:
            return s
        q.append(root)
        while q:
            node = q.pop()
            s += node.val
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)
            if not q:
                if not temp:
                    return s
                else:
                    q = temp
                    temp = deque()
                    s = 0
        return
        
        

