# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        root_num = ''
        start = 0
        while S[start].isdigit():
            root_num += S[start]
            start += 1
            if start == len(S):
                break
        div = [(0, int(root_num))]
        depth_counter = 0
        while start < len(S):
            if S[start] == '-':
                depth_counter += 1
                start += 1
            else:
                num = ''
                while S[start].isdigit():
                    num += S[start]
                    start += 1
                    if (start == len(S)):
                        break
                div.append((depth_counter, int(num)))
                depth_counter = 0
        res = TreeNode(int(root_num))
        track = res
        dicts = {0: res}
        for i in range(1, len(div)):
            depth, val = div[i][0], div[i][1]
            roots = dicts[depth - 1]
            if not roots.left:
                roots.left = TreeNode(val)
                dicts[depth] = roots.left
            else:
                roots.right = TreeNode(val)
                dicts[depth] = roots.right
        return res
