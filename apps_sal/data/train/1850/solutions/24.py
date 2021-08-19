class Solution:

    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        connected = collections.defaultdict(lambda: [])
        for (s, e) in edges:
            connected[s].append(e)
            connected[e].append(s)

        @functools.lru_cache(None)
        def get_to_father(node=0, father=None):
            sons = sorted([t for t in connected[node] if not t == father])
            to_ft_node = 0
            to_ft_sum = 0
            for son in sons:
                (node_nt, sum_nt) = get_to_father(son, node)
                to_ft_node += node_nt
                to_ft_sum += sum_nt
            to_ft_sum += to_ft_node
            to_ft_node += 1
            return (to_ft_node, to_ft_sum)
        to_ret = [0] * N

        def visit(node=N - 1, father=None, to_son_n=0, to_son_sum=0):
            sons = sorted([t for t in connected[node] if not t == father])
            ns_list = [get_to_father(t, node) for t in sons]
            all_node = sum([t[0] for t in ns_list])
            all_sum = sum([t[1] for t in ns_list])
            to_ret[node] = all_sum + all_node + to_son_sum + to_son_n
            for (son, (snode, ssum)) in zip(sons, ns_list):
                visit(son, node, to_son_n + all_node - snode + 1, to_ret[node] - ssum - snode)
        visit()
        return to_ret
