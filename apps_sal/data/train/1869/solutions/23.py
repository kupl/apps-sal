# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        leftChild = None
        rightChild = None
        if str.isnumeric(S):
            rootVal = S
        else:
            rootVal, S = S.split(\"-\", 1)
            S = \"-\" + S
            depths = re.split('\\d+', S)
            depths.pop()
            nodes = list(filter(None, re.split('-', S)))
            adjustedDepths = [d[1:] for d in depths]

            leftS = ''
            rightIdx = len(adjustedDepths)
            if '' in adjustedDepths[1:]:
                rightIdx = adjustedDepths[1:].index('') + 1
                rightS = ''
                for i in range(rightIdx, len(adjustedDepths)):
                    rightS = rightS + adjustedDepths[i] + nodes[i]
                rightChild=self.recoverFromPreorder(rightS)

            for i in range(rightIdx):
                leftS = leftS + adjustedDepths[i] + nodes[i]
            leftChild=self.recoverFromPreorder(leftS)
                

        return TreeNode(val=rootVal, left=leftChild, right=rightChild)
            
            

