# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def postorderTraversal(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """
         st, ans = [], []
         cur, last = root, None
         while cur or st:
             while cur:
                 st.append(cur)
                 cur = cur.left
             cur = st[-1]
             if not cur.right or cur.right == last:
                 ans.append(cur.val)
                 st.pop()
                 last = cur
                 cur = None
             else:
                 cur = cur.right
         return ans
         
