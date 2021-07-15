class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        if N == 0 or not edges:
            return [0]
        
        graph = {i: set() for i in range(N)}
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
        
        count = [1] * N
        subSums = [0] * N
        def countSubTree(node, parent):
            nonlocal count, subSums
            for child in (n for n in graph[node] if n != parent):
                countSubTree(child, node)
                count[node] += count[child]
                subSums[node] += subSums[child] + count[child]
            
        countSubTree(0, None)
        result = [0] * N
        result[0] = subSums[0]
        
        def countGlobal(node, parent):
            nonlocal result, count
            if parent != None:
                result[node] = result[parent] - count[node] + N - count[node]
            for child in (n for n in graph[node] if n != parent):
                countGlobal(child, node)
        countGlobal(0, None)
        return result
