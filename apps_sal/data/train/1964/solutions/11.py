class Solution:
     def printTree(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[str]]
         """
         # helper functions
         def depth(root):
             if root is None:
                 return 0
             return 1 + max(depth(root.left), depth(root.right))
         
         def fill(res, root, i, l, r):
             if root is None:
                 return
             res[i][(l + r) // 2] = str(root.val)
             fill(res, root.left, i + 1, l, (l + r) // 2)
             fill(res, root.right, i + 1, (l + r) // 2 + 1, r)
         
         # array filled with ""
         height = depth(root)
         width = pow(2, height) - 1
         ans = []
         for i in range(height):
             ans.append([])
             for j in range(width):
                 ans[i].append("")
         
         i = 0
         l = 0
         r = width
         
         fill(ans, root, 0, 0, width - 1)
         
 
         
         return ans

