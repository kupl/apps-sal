class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        tree = {}

        def add_edge(parent, child):
            children = tree.get(parent, [])
            children.append(child)
            tree[parent] = children
        for [a, b] in edges:
            add_edge(a, b)
            add_edge(b, a)

        if n == 1:
            return 1.0

        result = 1.0 if target == 1 else 0.0
        state = [(1, 1.0)]
        visited = set([1])
        for i in range(t):
            new_state = []
            for node, probability in state:
                children = [child for child in tree[node] if child not in visited]
                if len(children) == 0:
                    if node == target:
                        return probability
                    continue
                if node == target:
                    return 0
                visited.add(node)
                for child in tree[node]:
                    new_probability = probability * 1 / len(children)
                    if child == target:
                        result = new_probability
                    new_state.append((child, new_probability))
            state = new_state

        return result
