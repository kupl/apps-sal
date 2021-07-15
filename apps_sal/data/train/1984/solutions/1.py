
 class Solution:
     def buildTree(self, preorder, inorder):
         inorder_dict = {val:index for index,val in enumerate(inorder)}
 
         def buildTreeCore(pre_l, pre_r, in_l, in_r):
             if pre_l == pre_r:
                 return None
 
             root = TreeNode(preorder[pre_l])
             root_inorder_index = inorder_dict[root.val]
             root.left = buildTreeCore(pre_l+1,pre_l+1+root_inorder_index-in_l,\
                                     in_l,root_inorder_index)
             root.right = buildTreeCore(pre_l+1+root_inorder_index-in_l, pre_r,\
                                     root_inorder_index+1,in_r)
             return root
 
         return buildTreeCore(0, len(preorder), 0, len(preorder))
