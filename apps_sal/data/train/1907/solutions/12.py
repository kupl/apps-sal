
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned

        originalStack = []
        originalStack.append(original.right)
        originalStack.append(original.left)

        cloneStack = []
        cloneStack.append(cloned.right)
        cloneStack.append(cloned.left)

        while originalStack:
            currentCloneNode = cloneStack.pop()
            currentOriginalNode = originalStack.pop()

            if currentOriginalNode == target:
                return currentCloneNode

            if currentOriginalNode is not None:
                if currentOriginalNode.right:
                    originalStack.append(currentOriginalNode.right)
                    cloneStack.append(currentCloneNode.right)

                if currentOriginalNode.left:
                    originalStack.append(currentOriginalNode.left)
                    cloneStack.append(currentCloneNode.left)
