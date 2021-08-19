class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # 所有边按照类型排序， 类型为3的边有最高优先级
        edges.sort(key=lambda edge: edge[0], reverse=True)

        def build_graph(types):
            removed = set()
            neighbors = defaultdict(set)
            graph = []
            for (t, a, b) in edges:  # edge: t, a->b
                if t not in types:
                    continue
                if b in neighbors[a]:
                    removed.add((t, a, b))
                    continue
                # print((t, a, b))

                neighbors[a].add(b)
                neighbors[b].add(a)
                graph.append((t, a, b))
            # print('========')
            return removed, graph

        def find(f, a):
            if f[a] == 0:
                return a
            if f[a] != a:
                f[a] = find(f, f[a])
            return f[a]

        def generate_tree(graph, removed):
            f = defaultdict(int)
            nodes = set()
            for t, a, b in graph:
                nodes.add(a)
                nodes.add(b)
                fa, fb = find(f, a), find(f, b)
                if fa == fb:
                    removed.add((t, a, b))
                else:
                    f[fb] = fa

            return len(nodes) != n

        alice_removed, alice_graph = build_graph(set([1, 3]))
        bob_removed, bob_graph = build_graph(set([2, 3]))

        if generate_tree(alice_graph, alice_removed):
            return -1
        if generate_tree(bob_graph, bob_removed):
            return -1

        ans = len(alice_removed.union(bob_removed))
        return ans
