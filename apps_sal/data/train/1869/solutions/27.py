# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        #if the next node's num dashes increases , add as a child
        #also check next 
        
        #number of dashes tell you to move up/down
        
        #what does the order tell you?
        
        #there should only be 1 working node at each depth
        #keep a list of those
        #count the dashes, and then go to 1 above that
        
        
                
        nodes = []
        i = 0
        prev = \"\"
        for i in range(len(S)):
            if S[i] == \"-\" and prev == \"\":
                continue
            elif S[i] == \"-\":
                nodes.append(int(prev))
                prev = \"\"
            elif S[i] in list(\"0123456789\"):
                prev += S[i]
            else:
                assert False, f\"unrecognized char {S[i]}\"
        nodes.append(int(prev))
        
        depths = [0]
        prev = 0
        for i in range(len(S)):
            if S[i] in list(\"0123456789\") and prev == 0: #in the middle of a number, keep going
                continue
            if S[i] in list(\"0123456789\"): #ending a dash sequence, save the result
                depths.append(prev)
                prev = 0
            else: #middle of a dash sequence
                prev += 1
                
        assert len(nodes) == len(depths), \"should be same\"
        
        root = TreeNode(nodes[0])
        layers = [root] #keep track of the current node at each depth

        for i in range(1, len(nodes)):
            val = nodes[i]
            depth = depths[i]
            
            curr = TreeNode(val)
            assert depth <= len(layers)
            if depth == len(layers):
                layers.append(curr)
            else:
                layers[depth] = curr
            
            
            #go to the node 1 above
            parent = layers[depth-1]
            if parent.left == None:
                parent.left = curr
            else:
                assert parent.right == None, f\"{val}  {depth}   {parent}\"
                parent.right = curr
        return root
                            
            
            
