class Solution:
    
    def calcConnectedNodes(self, graph, node):
        visited = set()
        toVisit = []
        toVisit.append(node)
        while len(toVisit) != 0:
            
            curNode = toVisit.pop()
            if curNode in visited:
                continue
            visited.add(curNode)
            for i in range(len(graph[curNode])):
                if graph[curNode][i] == 1:
                    toVisit.append(i)
        return visited
    
    
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        initialSet = set(initial)
        maxNodesConnected = -1
        nodeToRemove = -1
        for node in initial:
            connectedNodes = self.calcConnectedNodes(graph, node)   
            intersected = connectedNodes.intersection(initialSet)
            # even if i removed this node, there are other nodes that will infect it, so no need
            if len(intersected) >= 2:
                continue
            if maxNodesConnected == -1 or len(connectedNodes) > maxNodesConnected or (len(connectedNodes) == maxNodesConnected and node < nodeToRemove):
                nodeToRemove = node
                maxNodesConnected = len(connectedNodes)
        if nodeToRemove == -1:
            return min(initial)
        return nodeToRemove

