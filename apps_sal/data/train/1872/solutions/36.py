
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        vals={}
        current=[root]
        vals[1]=root.val
        max1=0
        level=0
        cl=1
        
        while len(current):
            nodes=current
            children=[]
            sum1=0
            for node in nodes:
                
                if node.left:
                    children.append(node.left)
                    sum1+=node.left.val
                if node.right:
                    children.append(node.right)
                    sum1+=node.right.val
            
            vals[cl+1]=sum1
            if sum1>=max1:
                level=cl+1
                max1=sum1
            
            if len(children)>0:
                current=children
                cl+=1
            
            else:
                break
        
        
            
        return level

