class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        
    def union(self, index1, index2):
        root1 = self.find(index1)
        root2 = self.find(index2)
        if root1 == root2:
            return 0
        self.parents[root2] = root1
        return 1
    
    def find(self, index):
        if self.parents[index] != index:
            self.parents[index] = self.find(self.parents[index])
        return self.parents[index]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf1, uf2 = UnionFind(n), UnionFind(n)
        count_delete = 0
        count_union1, count_union2 = 0, 0
        
        for i, (weight, node1, node2) in enumerate(edges):
            if weight == 3:
                is_union = uf1.union(node1 - 1, node2 - 1)
                # is_union2 = uf2.union(node1 - 1, node2 - 1)
                # is_union = is_union1 and is_union2
                count_union1 += is_union
                count_union2 += is_union
                count_delete += 1 - is_union
        uf2.parents = copy.deepcopy(uf1.parents)
        count_union2 = count_union1
        
        for i, (weight, node1, node2) in enumerate(edges):
            if weight == 1:
                is_union = uf1.union(node1 - 1, node2 - 1)
                count_union1 += is_union
                count_delete += 1 - is_union
            elif weight == 2:
                is_union = uf2.union(node1 - 1, node2 - 1)
                count_union2 += is_union
                count_delete += 1 - is_union

        if count_union1 != n - 1 or count_union2 != n - 1:
            return -1
        return count_delete
                
            

