# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
      if not root: return 
      st=[[root,0]]
      ll=[]
      while st:
        r,l=st.pop(0)
        if l==len(ll) : ll.append([])
        ll[l].append(r.val)
        if r.left: st.append([r.left,l+1])
        if r.right:
          st.append([r.right,l+1])
      #print (ll,l)
      m=-1000
      re=0
      for i in range(l+1):
        n=sum(ll[i])
        if m<n:
          m=n
          re=i
      return re+1
        
      
      
      \"\"\"
        if not root:
          return []
        queue,res=[[root, 0]],[]
        while queue:
          #print (queue[0][0].val)
          node,level = queue.pop(0)
          
          if level == len(res):
            res.append([])
        
          res[level].append(node.val)
          if node.left:
            queue.append((node.left, level + 1))
          if node.right:
            queue.append((node.right, level + 1))
          
        return res[::-1]
      \"\"\"
