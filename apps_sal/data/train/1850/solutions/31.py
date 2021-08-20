import collections as clc
import typing as t


class Solution:

    def preorder(self, node: int, parent: t.Optional[int] = None) -> None:
        total_count = 0
        for child in self.graph[node]:
            if child == parent:
                continue
            count = self.preorder(child, node)
            self.distance[node] += count + self.distance[child]
            total_count += count
        self.subtree_count[node] = total_count + 1
        return total_count + 1

    def postorder(self, node: int, parent: t.Optional[int] = None) -> None:
        if parent is not None:
            self.distance[node] += self.distance[parent] - self.distance[node] - 2 * self.subtree_count[node] + self.n
        for child in self.graph[node]:
            if child == parent:
                continue
            self.postorder(child, node)

    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        self.n = N
        self.distance = [0] * N
        self.subtree_count = [0] * N
        self.graph = clc.defaultdict(list)
        for (a, b) in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)
        self.preorder(0)
        self.postorder(0)
        return self.distance
