# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        '''Q=[]
        Q.append(original)
        Q.append(\"LVL\")
        level=1
        pos=1
        my_dict={}
        while len(Q)>1:
            current=Q.pop(0)
            if current==\"NO\":
                Q.append(\"NO\")
                Q.append(\"NO\")
                pos+=2
                continue
            if current==target:
                my_dict[level]=pos
                break
            if current==\"LVL\":
                level+=1
                pos=0
                Q.append(\"LVL\")
                continue
            
            if current.left!=None:
                Q.append(current.left)
                pos+=1
            else:
                Q.append(\"NO\")
                pos+=1
            
            if current.right!=None:
                Q.append(current.right)
                pos+=1
            else:
                Q.append(\"NO\")
                pos+=1
        print(my_dict)
        
        Q=[]
        Q.append(cloned)
        Q.append(\"LVL\")
        level=1
        pos=1
        while len(Q)>1:
            current=Q.pop(0)
            if current==\"NO\":
                Q.append(\"NO\")
                Q.append(\"NO\")
                pos+=2
                continue
            if level in my_dict and pos==my_dict[level]:
                
                return current
            if current==\"LVL\":
                level+=1
                pos=0
                Q.append(\"LVL\")
                continue
            
            if current.left!=None:
                Q.append(current.left)
                pos+=1
            else:
                Q.append(\"NO\")
                pos+=1
            
            if current.right!=None:
                Q.append(current.right)
                pos+=1
            else:
                Q.append(\"NO\")
                pos+=1
                
           '''
        Q1=[]
        Q2=[]
        Q1.append(original)
        Q2.append(cloned)
        while len(Q1)>0:
            current1=Q1.pop(0)
            current2=Q2.pop(0)
            if current1==target:
                return current2
            if current1.left!=None:
                Q1.append(current1.left)
            if current1.right!=None:
                Q1.append(current1.right)
            if current2.left!=None:
                Q2.append(current2.left)
            if current2.right !=None:
                Q2.append(current2.right)
            
        
        
        
        
        
        
        
        
        
        
        
        
                

