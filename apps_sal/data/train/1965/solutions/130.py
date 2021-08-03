class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict

        def collapse(mapping, old_graph):
            new_graph = defaultdict(set)
            for node in old_graph:
                if node not in mapping:
                    mapping[node] = node

            duplicate_count = 0
            for s in old_graph:
                for e in old_graph[s]:
                    mapped_s = mapping[s]
                    mapped_e = mapping[e]

                    if mapped_e in new_graph[mapped_s] or mapped_s == mapped_e:
                        duplicate_count += 1
                        # print('collpase_cost', s, 'to', e, 'is mapped to', mapped_s, 'to', mapped_e)
                        continue

                    new_graph[mapped_s].add(mapped_e)

            for node in old_graph:
                if len(new_graph[mapping[node]]) == 0:
                    new_graph[mapping[node]] = []

            return new_graph, duplicate_count // 2

        def find_connected(graph):
            # return mapping
            mapping = dict()

            node_count = 0

            def dfs(cur_node, parent_node):
                nonlocal mapping, graph, node_count
                mapping[cur_node] = parent_node
                node_count += 1
                for next_node in graph[cur_node]:
                    if next_node not in mapping:
                        dfs(next_node, parent_node)

            edges_needed = 0
            for node in graph:
                if node not in mapping:
                    node_count = 0
                    dfs(node, node)
                    edges_needed += node_count - 1

            return mapping, edges_needed

        a_graph = defaultdict(set)
        b_graph = defaultdict(set)
        share_graph = defaultdict(set)
        point_set = set()
        for t, s, e in edges:
            point_set.add(s)
            point_set.add(e)
            if t == 1:
                a_graph[s].add(e)
                a_graph[e].add(s)
            elif t == 2:
                b_graph[s].add(e)
                b_graph[e].add(s)
            else:
                share_graph[s].add(e)
                share_graph[e].add(s)
        for point in point_set:
            if point not in a_graph:
                a_graph[point] = []
            if point not in b_graph:
                b_graph[point] = []

        costs = []
        share_mapping, edge_needed = find_connected(share_graph)
        new_share_graph, share_collapse = collapse(share_mapping, share_graph)
        costs.append(share_collapse - edge_needed)
        # print(share_collapse, edge_needed)

        for graph in [a_graph, b_graph]:
            # naming is ambiguous here

            new_graph, share_collpase = collapse(share_mapping, graph)
            # print(new_graph)
            sub_mapping, edge_needed = find_connected(new_graph)
            _, collpased = collapse(sub_mapping, new_graph)
            costs.append(share_collpase + collpased - edge_needed)
            # print(collpase, connect_cost, needed)
            # print(sub_mapping)
            if len(set(sub_mapping.values())) > 1:
                return -1

        return sum(costs)
