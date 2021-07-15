class Solution:
     def widthOfBinaryTree(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         
         widths = []
         
         def traverse(root, height, pos):
             nonlocal widths
             if root is None:
                 return
             if len(widths) < (height + 1):
                 widths.append([height, pos, pos])
             else:
                 if widths[height][1] > pos:
                     widths[height][1] = pos
                 if widths[height][2] < pos:
                     widths[height][2] = pos
             if pos == 0:
                 traverse(root.left, 1, -1)
                 traverse(root.right, 1, 1)
             else:
                 traverse(root.left, height + 1, (2 * pos - 1) if pos > 0 else (2 * pos))
                 traverse(root.right, height + 1, (2 * pos) if pos > 0 else (2 * pos + 1))
             
         traverse(root, 0, 0)
         ret = 0
         for width in widths:
             ret = max(ret, (width[2] - width[1]) if width[2] * width[1] < 0 else (width[2] - width[1] + 1))
         return ret
         

