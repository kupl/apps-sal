class Solution:
    
    # Check each vertex to see if its part of a cycle
    # If it is, it is not a safe vertex.
    
    # All nodes in that cycle are not considered to be safe vertices
    
    # Nodes that have no directed edges are also considered to be safe.
    
    # A node is considered safe it all its edges are to nodes that will eventually
    # become safe. So it one edge points to a safe node, but the other edge points to a 
    # cycle, that node is stil considered unsafe.
    
    # Even union find fails algo? Yes. You can group up safe nodes with cycles
    # Union find helps you prevent cycles, but not this application.
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        # If parent node i has no incoming edges (i,j) where parent (k) of 
        # node j is also a child of i, then it is not a cycle.
        
        # Let's say parent of i is safe
        # remove (i,j) from graphDict for child node j
        
        # Do so for all child of i, so that graphDict[i] has no more result 
        # (no more outgoing edges)
        
        #  Need to check all incoming edges though?
        
        # Just because its children are safe doesn't mean parent is safe.
        # The reverse is not true. If even one of its children is not safe, the 
        # parent is not safe. -> So if all children are safe, parent is safe.
        
        # Node j (child) is safe and in queue
        # i in reverseGraphDict[j], so remove (i,j) from graphDict
        # Loop. If all (i,j) is removed from graphDict, so 
        # graphDict[i] contains empty set(), then parent is also successfully safe.
        
        #    0     1    2   3   4   5  6      all parents
        # [[1,2],[2,3],[5],[0],[5],[],[]]    all children     
        \"\"\"
        N = len(graph)
        safe = [False] * N

        graph = list(map(set, graph))
        rgraph = [set() for _ in range(N)]
        q = collections.deque()

        for i, js in enumerate(graph):
            if not js:
                q.append(i)
            for j in js:
                rgraph[j].add(i)

        while q:
            j = q.pop()
            safe[j] = True
            for i in rgraph[j]:
                graph[i].remove(j)
                if len(graph[i]) == 0:
                    q.append(i)

        return [i for i, v in enumerate(safe) if v]\"\"\"
        
        
        
        
        
        N = len(graph)
        safe = [False] * N
        
        graph = list(map(set,graph))
        print(graph)
        for elem in graph:
            print(elem)
        reverseGraphDict = [set() for _ in range(N)]

        safeQueue = collections.deque()
        
        for parent, children in enumerate(graph):
            # If there is no children (empty[]), terminal node
            if not children:
                safeQueue.append(parent)
                
            for child in children:
                # Don't do dfs here
                reverseGraphDict[child].add(parent) # a child can have multiple parents
                
                
                
        while safeQueue:
            child = safeQueue.pop()
            safe[child] = True
            for parent in reverseGraphDict[child]:
                graph[parent].remove(child)
                
                # Parent is safe too, so push it into queue
                if len(graph[parent]) == 0:
                    #safe[parent] = True # Wil be taken care at top of loop
                    safeQueue.append(parent)
                
        return [idx for idx, boolean in enumerate(safe) if boolean == True]
            
        \"\"\"
        # Try DFS. Use a set to keep track of nodes already seen
        seenSet = set()
        safeList = []
        
        # Add parent to seenSet
        # Iterate over all connections to children from parent
        # dfs for each of those connections
        
        def dfs(parent):
            nonlocal graph
            nonlocal seenSet
            
            if parent in seenSet: # Already discovered before
            
            seenSet.add(parent)
            
            for edge in graph:
                if edge[0] == parent:
                    dfs(edge[1])
            
        
        
        
        \"\"\"
        '''
        # Loop over all nodes in graph, make them their own group
        for edge in graph:
            parent = edge[0]
            
            # group.newGroup(parent)
        
        
        for edge in graph:
            parent = edge[0]
            child = edge[1]'''
            
            # group parent and child together
            
            # if child is already grouped with parent (cycle),
            # Those nodes in the group cannot be part of the answer.
            
            # But if the parent/child has only one connection to all 
            # the nodes within the group that has the cycle, that node
            # (though connect) is technically safe.
            
            
