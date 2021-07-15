class Solution:
     def printTree(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[str]]
         """
         def getHeight(root):
             if not root: return 0
             return 1 + max(getHeight(root.left), getHeight(root.right))
         
         h = getHeight(root)
         w = 2**h - 1
         res = [[""]*w for _ in range(h)]
         
         def preorder(root, start, end, h):
             if not root: return 
             mid = (start + end) // 2
             res[h][mid] = str(root.val)
             preorder(root.left, start, mid, h+1)
             preorder(root.right, mid+1, end, h+1)
         
         preorder(root, 0, w, 0)
         return res
             
             

