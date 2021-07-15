class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        ptr = 0
        def traverse(level: int) -> TreeNode:
            nonlocal ptr
            nextLevel = 0
            while ptr < len(S) and S[ptr] == '-':
                nextLevel += 1
                ptr += 1
                
            if level == nextLevel: 
                val = ''
                while ptr < len(S) and S[ptr] != '-':
                    val += S[ptr]
                    ptr += 1
                node = TreeNode(int(val))
                node.left = traverse(level+1)
                node.right = traverse(level+1)
                return node
            else:
                ptr -= nextLevel
                return None

        return traverse(0)

