class Solution:
     def widthOfBinaryTree(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         
         def get_max_width(root, width, level, d):
             if not root:
                 return
             
             d[level].append(width)
             # I want the nodes of a level numbered from 0.. 2^n-1
             get_max_width(root.left, 2*width, level + 1, d)
             get_max_width(root.right, 2*width + 1, level + 1, d)
         
         from collections import defaultdict
         d = defaultdict(list)
         
         get_max_width(root, 0, 0, d)
         
         print(d)
         max_width = 0
         for level, elements in list(d.items()):
             if elements: 
                 # if the len of elements is 1 i will still get width 1
                 elements.sort()
                 curr_width = elements[-1] - elements[0] + 1
                 max_width = max(max_width, curr_width)
         
         return max_width
             

