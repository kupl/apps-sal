import queue

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        \"\"\"
        Obs:
        1. Clearly, each note that belongs to the cycle is wrong
        If node is a leaf (terminal node), then it's eventually safe.
        If we remove this node, some other nodes might become leaves, if so, they are eventuall safe as well
        \"\"\"
        
        # We need transposition of the graph (directed graph with reversed edges), to be able to decrease out_deg for out predecessors
        graph_t = [[] for _ in range(len(graph))]
        for origin, adj_list in enumerate(graph):
            for dest in adj_list:
                graph_t[dest].append(origin)
        
        deg_out = [0 for _ in range(len(graph))]
        deg_out = [len(adj_list) for adj_list in graph]
        
        terminal_nodes = queue.Queue()
        for terminal_node in [node for node, d_out in enumerate(deg_out) if d_out == 0]:
            terminal_nodes.put(terminal_node)
        res = []
        while not terminal_nodes.empty():
            node = terminal_nodes.get()
            for dest in graph_t[node]:
                deg_out[dest] -= 1
                if deg_out[dest] == 0:
                    terminal_nodes.put(dest)
            
            res.append(node)
        
        return sorted(res)
        
