class Solution:

    def __init__(self):
        self.safe_nodes = set()
        self.unsafe_nodes = set()

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        def is_safe(node, stack=[]):
            if not graph[node] or node in self.safe_nodes:
                self.safe_nodes.add(node)
                return True
            elif node in self.unsafe_nodes:
                return False
            else:
                if node in stack:
                    self.unsafe_nodes |= set(stack)
                    return False
                stack.append(node)
                if all([is_safe(child) for child in graph[node]]):
                    self.safe_nodes.add(node)
                    stack.pop()
                    return True
                else:
                    self.unsafe_nodes.add(node)
                    stack.pop()
                    return False
        for node in range(len(graph)):
            is_safe(node)
        return sorted(list(self.safe_nodes))
