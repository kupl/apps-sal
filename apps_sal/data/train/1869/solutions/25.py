# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def dfs(s, level):
    if not s:
        return
    if len(s) == 1:
        return TreeNode(int(s[0]))
    ss = []
    nex = []
    c = 0
    l = 0
    for i in range(1, len(s)):
        if s[i] != \"-\":
            if len(ss) == level+1:
                nex.append(s[l:i-level-1])
                l = i
                c += 1
                if c == 2:
                    nex.append(s[i:])
                    break
            ss.clear()
        else:
            ss.append(\"-\")
    if c != 2:
        nex.append(s[l:])
        
    root = TreeNode(int(nex[0]))
    nex = nex[1:]
    if nex:
        root.left = dfs(nex[0], level+1)
        nex = nex[1:]
    if nex:
        root.right = dfs(nex[0], level+1)
        nex = nex[1:]
    return root


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        return dfs(S, 0)
