class Solution:
     def widthOfBinaryTree(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         if root is None: return 0;
         
         q = [(root, 0)];
         left = 0;
         right = 0;
         res = 1;
         
         while q:
             qLength = len(q);
             
             for i in range(qLength):
                 node, index = q.pop(0);
                 if i == 0:
                     left = index;
                 if i == qLength - 1:
                     right = index;
                 
                 if node.left is not None:
                     q.append((node.left, (2*index)+1));
                 if node.right is not None:
                     q.append((node.right, (2*index)+2));
                     
             res = max(res, right-left+1);
         
         return res;

