import queue
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        
        red = self.create_adj(red_edges, n)
        blue = self.create_adj(blue_edges, n)
        
        dist_array = [-1 for _ in range(n)]
        dist_array[0] = 0
        q = queue.Queue()
        self.bfs(red, blue, \"blue\", dist_array)
        self.bfs(red, blue, \"red\", dist_array)
        return dist_array
        
    def bfs(self, red, blue, color, A):
        visited_red = set()
        visited_blue = set()
        q = queue.Queue()
        if color == \"blue\":
            visited_blue.add(0)
        else:
            visited_red.add(0)
        q.put((0,0, color))
        
        while(q.qsize() != 0):
            cur = q.get()
            cur_node = cur[0]
            cur_len = cur[1]
            cur_color = cur[2]
            if cur_color == \"red\":
                for node in red[cur_node]:
                    if node not in visited_red:
                        visited_red.add(node)
                        q.put((node, cur_len + 1, \"blue\"))
                        if A[node] >= 0:
                            A[node] = min(A[node], cur_len + 1)
                        else:
                            A[node] = cur_len + 1
                cur_color = \"blue\"
            else:
                for node in blue[cur_node]:
                    if node not in visited_blue:
                        visited_blue.add(node)
                        q.put((node, cur_len + 1, \"red\"))
                        if A[node] >= 0:
                            A[node] = min(A[node], cur_len + 1)
                        else:
                            A[node] = cur_len + 1
                cur_color = \"red\"
        

        
        
        
    def create_adj(self, nodes, n):
        adj = [[] for node in range(n)]
        for i in range(len(nodes)):
            adj[nodes[i][0]].append(nodes[i][1])
        
        return adj
