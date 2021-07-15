# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def check(root, total, limit):
            #   返回：子树的路径的最大值
            if root == None:
                return None
            total += root.val

            #   当前是叶节点，判断状态并返回
            if root.left == root.right:
                if total < limit:
                    return None
                else:
                    return root
            
            flag1 = 0   #   0-不考虑、-1为失败、1为成功
            flag2 = 0
            if root.left:
                root.left = check(root.left,  total, limit)
                flag1 = 1 if root.left  else -1
            if root.right:
                root.right= check(root.right, total, limit)
                flag2 = 1 if root.right else -1

            if flag1 > 0 or flag2 > 0:
                return root
            else:
                return None
        
        rtv = check(root, 0, limit)
        return rtv



