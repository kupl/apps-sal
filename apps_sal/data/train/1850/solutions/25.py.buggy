class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(N)}
        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)            
        
        root = 0

        subtree_sum_count = {i: (0,0) for i in range(N)}
        visited = set()
        def subtree(vertex: int, parent = None):
            if len(adjList[vertex]) == 1 and adjList[vertex][0] == parent:
                subtree_sum_count[vertex] = 0, 0
            elif vertex not in visited:
                subtrees = [subtree(child, vertex) for child in adjList[vertex] if child != parent]
                subtree_sum_count[vertex] = sum(tree[0] + tree[1] + 1 for tree in subtrees), sum(tree[1] + 1 for tree in subtrees)
                visited.add(vertex)
                
            return subtree_sum_count[vertex]
        
        subtree(root)
                
        distances = [0] * N
        distances[root] = subtree_sum_count[root][0]
        
        queue = collections.deque([(root, child) for child in adjList[root]])
        
        while len(queue) > 0:
            parent_node, vertex = queue.popleft()
            queue.extend([(vertex, child) for child in adjList[vertex] if child != parent_node])
            if vertex == root:
                continue
            p_node = distances[parent_node], subtree_sum_count[parent_node][1]
            temp = p_node[0] - subtree_sum_count[vertex][0] - subtree_sum_count[vertex][1] - 1, \\
                   N - subtree_sum_count[vertex][1] - 1
            
            distances[vertex] = subtree_sum_count[vertex][0] + sum(temp)
            
        return distances
