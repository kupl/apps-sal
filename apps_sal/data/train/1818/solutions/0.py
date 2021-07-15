# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        nonlocal ls
        ls=[]
        di={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
        def helper(root,s):
            if(root==None):
                return None
            nonlocal ls
            if(root.left==None and root.right==None):
                ls.append(di[root.val]+s)
            
            helper(root.left,di[root.val]+s)
            helper(root.right,di[root.val]+s)
            
        helper(root,\"\")
        print(ls)
        # tem=sorted(ls)[0]
        tem=sorted(ls)
        return tem[0]
        # ans=\"\"
        # for i in tem:
        #     ans+=str(di[int(i)])
        # return ans
            
