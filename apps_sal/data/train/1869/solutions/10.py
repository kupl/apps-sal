# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Input: \"1-2--3--4-5--6--7\" 
i = 6, c=2, num=4, level = 1
j = 
'''
def getNext(s, i):
    c = 0

    while(i<len(s) and s[i]=='-'):
        i+=1
        c+=1
    num = []
    if i==len(s):
        return -1, -1, -1
    while(i<len(s) and s[i]!='-'):
        num.append(s[i])
        i+=1

    return c, int(''.join(num)), i

c, num, i = 0, 0, 0
def solve(s, level):
    
    nonlocal c,num,i
    c,num,j = getNext(s,i)
    
    if c==-1 or c<level:
        return None
    node = TreeNode(num)
    i = j
    node.left = solve(s,level+1)
    node.right = solve(s,level+1)
    
    return node   


class Solution:
    
    def recoverFromPreorder(self, S: str) -> TreeNode:
        nonlocal c,num,i
        c, num, i = 0, 0, 0
        return solve(S, 0)
