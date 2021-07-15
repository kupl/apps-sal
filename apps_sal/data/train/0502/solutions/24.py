from collections import defaultdict
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        edges = defaultdict(list)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if(graph[i][j] == 1):
                    edges[i].append(j)
        #maps nodes to their color  
        colors = defaultdict(int)
        #counts the number of nodes in that colored connected component
        nodes_in_colors = defaultdict(int)
        color = 1
        for node in initial:
            if(colors[node] == 0):
                colors[node] = color
            else:
                continue
            stack = [node]
            visited = set()
            curr_infected = 0
            while(stack):
                curr = stack.pop()
                curr_infected += 1
                for neigh in edges[curr]:
                    if(neigh not in visited):
                        stack.append(neigh)
                        visited.add(neigh)
                        colors[neigh] = color
            nodes_in_colors[color] = curr_infected
            color += 1
        #maps color to initial nodes of that color
        initial_color = defaultdict(list)
        for node in initial:
            initial_color[colors[node]].append(node)
        print(initial_color)
        unique_color = defaultdict(int)
        #only look for unique colors/ components with unique colors
        for node in initial:
            unique_color[colors[node]] += 1
        
        unique = []
        for color in unique_color:
            if(unique_color[color] == 1):
                unique.append(initial_color[color][0])
        if(len(unique) == 0):
            return min(initial)
        
        max_infected = 0
        min_node = float('inf')
        print(unique)
        for node in unique:
            if(nodes_in_colors[colors[node]] >= max_infected):
                max_infected = nodes_in_colors[colors[node]]
                min_node = min(node, min_node)
        return min_node
                
                

