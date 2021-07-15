# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     # def buildTree(self, preorder, inorder):
     #     """
     #     :type preorder: List[int]
     #     :type inorder: List[int]
     #     :rtype: TreeNode
     #     """
     #     if (not preorder):
     #         return None
     #     root_val = preorder[0]
     #     root = TreeNode(root_val)
     #     left_count = inorder.index(root_val)
     #     root.left = self.buildTree(preorder[1:left_count + 1], inorder[:left_count])
     #     root.right = self.buildTree(preorder[left_count + 1:], inorder[left_count + 1:])
     #     return root
         
 
     """
     栈
     读取前序序列，当不确定节点的左子树是否处理完毕时将节点压栈
     上述操作将保持栈内元素关系：任意时刻，栈内的后入栈元素位于先入栈元素的左子树中
     当元素的左子树已经全部处理完时将其出栈，此时应该继续处理它的右子树（如果存在的话）
     判定元素的左子树是否已经处理完毕，需要中序序列，对于中序序列中的任意元素 j ，其左子树位于 [0, j - 1] 中
     因此，当栈顶元素等于中序序列的当前元素 j （中序的 [0, j - 1] 已经处理）时，表明栈顶元素的左子树已经处理完毕
     """
     def buildTree(self, preorder, inorder):
         """
         :type preorder: List[int]
         :type inorder: List[int]
         :rtype: TreeNode
         """
         if (not preorder):
             return None
         stack = []
         i, j = 0, 0
         # 前序序列的第一个元素即树的根节点
         root = TreeNode(preorder[0])
         cur = root
         stack.append(cur)
         i += 1
         # 循环的本步是否进行出栈操作
         out_stack = False
         # 读取前序序列， preorder[-1] 是最右节点，当这个节点构造完成（ i == len(preorder) ），整颗树就完成了，结束循环
         while (i < len(preorder)):
             if (stack and stack[-1].val == inorder[j]):
                 # 出栈操作，相当于从递归返回
                 # cur 的左子树已经处理完毕
                 # 如果cur有右子树，那么下一步将进入下面的else的if(out_stack)语句块
                 # 如果cur没有右子树，那么下一步将继续进行本语句块的出栈操作
                 cur = stack.pop()
                 out_stack = True
                 j += 1
             else:
                 # 入栈操作，相当于进入递归
                 # stack[-1] 的左子树未处理完毕
                 if (out_stack):
                     # 上一步执行了出栈操作，表明cur的左子树已经处理完毕，需要处理其右子树
                     # 相当于进入cur右子树的递归
                     # cur有右子树，preorder[i]是cur右子树的根节点
                     cur.right = TreeNode(preorder[i])
                     cur = cur.right
                 else:
                     # 上一步不是出栈，表明cur的左子树尚未处理
                     # 相当于进入cur左子树的递归
                     cur.left = TreeNode(preorder[i])
                     cur = cur.left
                 stack.append(cur)
                 out_stack = False
                 i += 1
         return root
                     
                 
