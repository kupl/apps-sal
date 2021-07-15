# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def buildTree(self, preorder, inorder):
         """
         :type preorder: List[int]
         :type inorder: List[int]
         :rtype: TreeNode
         """
         if len(inorder) == 0:
             return
         #构建元素值为key, index为value的hashmap
         HashMap = {}
         for i in range(len(inorder)):
             HashMap[inorder[i]] = i
         
         root = self.build(HashMap, inorder, 0, len(inorder)-1, preorder, 0, len(preorder)-1)
         return root
     
     def build(self, HashMap, inorder, istart, iend, preorder, pstart, pend):
         if istart>iend or pstart > pend:
             return None
 
         root = TreeNode(preorder[pstart])
         mid_index = HashMap[root.val]
         left_size = mid_index - istart
         right_size = iend - mid_index
         root.left = self.build(HashMap, inorder, istart, mid_index-1, preorder, pstart+1, pstart+left_size)
         root.right = self.build(HashMap, inorder, mid_index+1, iend, preorder, pend-right_size+1, pend)
         return root
