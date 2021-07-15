from copy import deepcopy
from collections import Counter
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        edges.sort(reverse = True)
        
        graph = [i for i in range(n)]
        
        def p(i,graph):
            level = 0
            while i != graph[i]:
                i = graph[i]
                level += 1
            return i,level
        
        i = 0
        res = 0
        g = graph
        graph_a = graph_b = None
        
        while i < len(edges):
            t,a,b = edges[i]
            if t == 2 and (i == 0 or edges[i-1][0] != 2):
                graph_b = deepcopy(graph)
                g = graph_b
            if t == 1 and (i == 0 or edges[i-1][0] != 1):
                graph_a = deepcopy(graph)
                g = graph_a
            ap,al = p(a-1,g)
            bp,bl = p(b-1,g)
            if ap == bp: res += 1
            elif ap == a-1: g[ap] = bp
            elif bp == b-1: g[bp] = ap
            elif al < bl: g[ap] = bp
            else: g[bp] = ap
            i += 1
            
        if not graph_a:
            graph_a = deepcopy(graph)
        if not graph_b:
            graph_b = deepcopy(graph)
        
        for i in range(n):
            graph_a[i] = p(i,graph_a)[0]
            graph_b[i] = p(i,graph_b)[0]
            
        a = Counter(graph_a)
        b = Counter(graph_b)
        if len(a) > 1 or len(b) > 1: return -1
        return res
