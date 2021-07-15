# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        if original == target:
            return cloned
        node = None
        if original.left:
            node = self.getTargetCopy(original.left, cloned.left, target)
        if not node and original.right:
            node = self.getTargetCopy(original.right, cloned.right, target)
        return node
            
        \"\"\"
        def _findNodeAndReturnPath(root, tgt, path):
            if not root:
                return ''
            if root == tgt:
                return path
            #print(' looking left for node %d' % root.val)
            lpath = _findNodeAndReturnPath(root.left, tgt, path + 'L')
            if lpath:
                #print(' found target at node %d, Lpath=%s' % (root.val, lpath))
                
                return lpath
            #print(' looking right for node %d' % root.val)
            rpath = _findNodeAndReturnPath(root.right, tgt, path + 'R')
            if not rpath:
                return ''
            #print(' found target at node %d, Rpath=%s' % (root.val, rpath))
            return rpath
        #print(' path to node=%d is %s' % (target.val, 'path'))
        path = _findNodeAndReturnPath(original, target, '')
        print(' path to node=%d is %s' % (target.val, path))
        curr = cloned
        for xc in path:
            if xc == 'L':
                curr = curr.left
            else: # if xc == 'R':
                curr = curr.right
        return curr
        \"\"\"
