class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        if N == 1:
            return [0]
        graph_dict = {}
        for pair in edges:
            left, right = pair[0], pair[1]
            graph_dict[left] = [right] + graph_dict.get(left, [])
            graph_dict[right] = [left] + graph_dict.get(right, [])
        memo_dict = {}
        ans = []
        for i in range(N):
            ans += [self.helper(i, None, graph_dict, memo_dict)[0]]
        return ans

    def helper(self, node, parent, graph_dict, memo_dict):
        if (graph_dict[node] == [parent]):
            return (0, 1)  # depth,num_nodes
        elif (node, parent) in memo_dict:
            return memo_dict[(node, parent)]
        else:
            found_sum = 0
            num_nodes = 1
            for neighbor in graph_dict[node]:
                if neighbor != parent:
                    (curr_sum, curr_nodes) = self.helper(neighbor, node, graph_dict, memo_dict)
                 #   print((node,parent,curr_sum,curr_nodes))
                    found_sum = (1 * curr_nodes) + curr_sum + found_sum
                    num_nodes += curr_nodes
            memo_dict[(node, parent)] = (found_sum, num_nodes)
            return (found_sum, num_nodes)
