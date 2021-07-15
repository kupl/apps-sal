# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        # for all possible y, we need to check if we can win
        # we can return early if we can do that
        
        # now what to do after selecting a y
        # we have three choices:
        # select left, right or parent 
        # we can simulate what happens in each case
        # we can return True if any of those choices
        # return True
        # we also have to simulate what happens if it is not
        # our turn, in that case, we have to choose the minimum
        # i.e. return false if anything is false
        # since we are trying to maximize our profit
        
        
        # we also need a way to simulate which node is colored what 
        # atleast temporarily
        
        # we can store a tuple for nodes
        # if 0, uncolored
        # if 1, blue
        # if -1, red
        
        # exit conditions
        # if no nodes left to be colored
        # 
        
        if not root:
            return False
        
        from collections import defaultdict
        
        graph = defaultdict(list)
        
        def convert_tree_to_graph(root, parent=None):
            if not root:
                return None
            if parent:
                # creating bi-directional edges
                graph[parent].append(root)
                graph[root].append(parent)
            if root.left:
                convert_tree_to_graph(root.left, root)
            if root.right:
                convert_tree_to_graph(root.right, root)
                    
        convert_tree_to_graph(root)
    
        # now we have the graph, we just need to find the node that player 1 selected
        # and count its trees in each direction
        node = None
        for g, v in list(graph.items()):
            if g.val == x:
                node = g
                break
        
        def count_nodes_in_subtree(node, visited):
            #return count
            if node in visited or node.val==x:
                return 0
            visited.add(node)
            count = 0
            for neighbor in graph[node]:
                if neighbor not in visited:
                    count += count_nodes_in_subtree(neighbor, visited)
            return count + 1 
                    
        subtrees = []
        max_subtree = -1
        #print (node, subtrees)
        for subtree in graph[node]:
            ans = count_nodes_in_subtree(subtree, set())
            subtrees.append(ans)
            max_subtree = max(max_subtree, ans)
        
        return n - max_subtree < max_subtree
            
            
        if not subtrees:
            return False
        
        if len(subtrees)== 1 and subtrees[0]>1 : # only 1 subtree and we chose it
            return True 
        
        
        
        return False
            
        
        
        
                    
                    
        
        

