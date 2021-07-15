class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        #Graph represented as an adjaency matrix        
        #Loop through infected
        #Simulate condition of what would happen if only this infected node is removed
        #If num infected is the new min -> then we have a potential answer
        
        infected_nodes = set(initial)
        max_infected = len(graph)
        node_to_remove = initial[0]
        
        for infected_node in initial:
            infected_nodes.remove(infected_node)
            infected = set()
            for node in infected_nodes:
                self.dfs(node, graph, infected)
                
            infected_nodes.add(infected_node)
            if len(infected) < max_infected or (len(infected) == max_infected and infected_node < node_to_remove):
                node_to_remove = infected_node
                max_infected = len(infected)
        return node_to_remove
        #Loop through the infected nodes
        #Do a traversal to simulate an \"infection\"
        #Count number of nodes infected and track max infected
        
    def dfs(self, node, graph, infected):
        infected.add(node)
        for col, val in enumerate(graph[node]):
            if val == 1 and col not in infected:                
                self.dfs(col, graph, infected)

