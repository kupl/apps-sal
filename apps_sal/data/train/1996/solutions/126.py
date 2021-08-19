class Solution:

    def __init__(self):
        self.d = {}
        self.safe_nodes = {}

    def safe_finder(self, cur_node):
        if len(self.d[cur_node]) == 0:
            self.safe_nodes[cur_node] = True
            return True
        for n in self.d[cur_node]:
            print(cur_node, n)
            if n == cur_node:
                self.safe_nodes[cur_node] = False
                return False
            if n in self.safe_nodes.keys():
                if self.safe_nodes[n] == False:
                    self.safe_nodes[cur_node] = False
                    return False
            else:
                self.safe_nodes[n] = False
                tmp = Solution.safe_finder(self, n)
                if tmp == False:
                    self.safe_nodes[cur_node] = False
                    return False
        self.safe_nodes[cur_node] = True
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        for i in range(len(graph)):
            node = graph[i]
            self.d[i] = []
            for edge in node:
                self.d[i].append(edge)
        for k in self.d.keys():
            Solution.safe_finder(self, k)
        answer = []
        for (k, v) in self.safe_nodes.items():
            if v == True:
                answer.append(k)
        return sorted(answer)
