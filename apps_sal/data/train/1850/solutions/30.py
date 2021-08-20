class Solution:

    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        edges_dict = dict()
        for i in range(N):
            edges_dict[i] = []
        for edge in edges:
            edges_dict[edge[0]].append(edge[1])
            edges_dict[edge[1]].append(edge[0])
        dp_dict = dict()

        def dp(node, src):
            if (node, src) in dp_dict:
                return dp_dict[node, src]
            tgt_num = 1
            tgt_sum = 0
            for tgt in edges_dict[node]:
                if tgt == src:
                    continue
                else:
                    temp = dp(tgt, node)
                    tgt_num += temp[0]
                    tgt_sum += temp[0] + temp[1]
            dp_dict[node, src] = (tgt_num, tgt_sum)
            return dp_dict[node, src]
        results = [0] * N
        for node in range(N):
            for tgt in edges_dict[node]:
                results[node] += sum(dp(tgt, node))
        return results
