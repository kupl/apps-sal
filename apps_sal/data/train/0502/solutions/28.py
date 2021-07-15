class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        minNode = -1
        maxSpread = 0
        for node in initial:
            testInit = initial.copy()
            testInit.remove(node)
            touch,testSpread = touchAnyNodes([node],graph,testInit)
            #print (str(node) + \" \" + str(touch) + \" \" + str(testSpread) )
            if not touch:
                if testSpread > maxSpread or (testSpread == maxSpread and node < minNode):
                    maxSpread = testSpread
                    minNode = node
        if maxSpread == 0:
            initial.sort()
            return initial[0]
        return minNode

def touchAnyNodes(visited,graph,infected) -> (bool,int):
    newVisited = visited.copy()
    for node in visited:
        for idx in range(len(graph[node])):
            if graph[node][idx] == 1 and (not idx in visited) and (not idx in newVisited):
                if idx in infected:
                    return True,0
                newVisited.append(idx)
    if len(newVisited) == len(visited):
        return False,len(visited)
    return touchAnyNodes(newVisited,graph,infected)

