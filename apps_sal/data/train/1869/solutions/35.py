# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        first = S.find(\"-\")
        if \"-\"*len(S)==S:
            return None
        if first<0:
            if len(S)<1 :
                return None
            else:
                return TreeNode(int(S))
        
        root = TreeNode(int(S[:first]))
        stack = [(root, 0)]
        prev=0
        S = S[first:]
        while len(S)>0:
            curr_ = 0
            for idx, char in enumerate(S):
                if char==\"-\":
                    curr_+=1
                else:
                    break
            S = S[idx:]
            curr_num = \"\"
            for idx, char in enumerate(S):
                if char==\"-\":
                    break
                else:
                    curr_num+=char
            curr_num = TreeNode(int(curr_num))
            S = S[idx:]
            if prev < curr_: # then this is a child
                stack[-1][0].left = curr_num
                stack.append((curr_num, curr_))
            else:
                last = stack[-1]
                while stack and stack[-1][1]+1 >= curr_: # this is a right node or go one step up
                    # while checking where to attach the right node, we need to go one step above when we rech equality
                    # we need to go one step up,  if there is an equality hence on lhs there is the +1
                    last = stack.pop()
                last[0].right = curr_num
                stack.append((last[0].right, curr_))
            
            
            prev = curr_
            if len(S)==1:
                break
        
        return root
            
