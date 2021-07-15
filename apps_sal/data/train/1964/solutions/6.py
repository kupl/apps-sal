"""
 满二叉树定位
 """
 
 def tree_height(tr, h):
     if not tr: return h
     lh, rh = tree_height(tr.left, h + 1), tree_height(tr.right, h + 1)
     return max(lh, rh)
     
 
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
         w = 2 ** h - 1
         w = (1 << h) - 1
         res = [[""]* w for _ in range(h)]
         
         def inorder(root,start,end,lev):
             if not root: return
             mid = (start + end) >> 1
             res[lev][mid] = str(root.val)
             inorder(root.left, start, mid, lev+1)
             inorder(root.right, mid + 1, end, lev+1)
         inorder(root, 0, w, 0)
         return res
         
         
         
         
         if (not root.left) and (not root.right): return [[str(root.val)]]
         th = tree_height(root, 0)
         w = (1 << th) - 1
         res = [[""] * w for i in range(th)]
         
         que = [(root, 0)]
         level = th - 1
         beg, end = 0, 1
         step = 1 << th
         while beg < end:
             level_cnt = 0
             for k in range(beg, end):
                 nd, i = que[k]
                 # print(th - 1 - level, step, nd.val, i, ((i + 1) * step) - (step >> 1) - 1)
                 #  ((i + 1) * step) - (step >> 1) - 1 # 第i个step块的中间位置，0始下标
                 res[th - 1 - level][((i + 1) * step) - (step >> 1) - 1] = str(nd.val)
                 if nd.left:
                     que.append((nd.left, i << 1))
                     level_cnt += 1
                 if nd.right:
                     que.append((nd.right, (i << 1) + 1))
                     level_cnt += 1
                 beg += 1
             level -= 1
             step >>= 1
             end += level_cnt
         return res
                     
 """
 [1,2]
 [1,2,3, null, null,4,5]
 [1]
 """
 
         
