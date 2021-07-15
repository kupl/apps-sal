class Node:
    
    def __init__(self, row, col, parent=None):
        self.row = row
        self.col = col
        self.parent = parent or self
        self.rank = 0
        self.size = 1
    
    def __eq__(self, other):
        return other.row == self.row and other.col == self.col
    
    def __hash__(self):
        return hash((self.row, self.col))
    
    def __repr__(self):
        return f\"Node: {(self.row,self.col)}, Rank {self.rank}, Size {self.size}\"


class UnionFind:
    def __init__(self):
        self.count = 0
        self.rc_to_node = {}
        self.disjoint_sets=set()
    
    def find(self, row, col):
        
        val = (row,col)
        node = self.rc_to_node.get(val)
        if not node:
            node = Node(row,col)
            self.rc_to_node[val] = node
            self.disjoint_sets.add(node)
            self.count+=1
        elif node.parent != node:
            node.parent = self.find(node.parent.row, node.parent.col)
        
        return node.parent
    
    def union(self, fr,fc,sr,sc):
        first = self.find(fr,fc)
        second = self.find(sr,sc)
        
        if first == second:
            return
        
        if first.rank > second.rank:
            first,second = second, first
        
        first.parent = second
        second.rank+=first.rank == second.rank
        second.size+=first.size
        self.disjoint_sets.remove(first)
        self.count-=1
        #print(f\"{self.disjoint_sets}, {self.rc_to_node}\" )


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        mrow,mcol = len(grid), len(grid[0])
        
        zero_indexes = []
        uf = UnionFind()
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if not col:
                    zero_indexes.append((i,j))
                    continue
                uf.find(i,j)

                for dr,dc in direction:
                    r,c = dr+i, dc+j
                    if 0<=r<mrow and 0<=c<mcol and grid[r][c]:
                        uf.union(i,j,r,c)
        
        max_size = 0
        for c in uf.disjoint_sets:
            max_size = max(max_size,c.size)
        
        for i,j in zero_indexes:
            size = 0 
            parents = set()
            for dr,dc in direction:
                r,c = dr+i, dc+j
                if 0<=r<mrow and 0<=c<mcol and grid[r][c]:
                    node = uf.find(r,c)
                    if (node.row,node.col) not in parents:
                        size+=node.size
                        parents.add((node.row,node.col))
            
            max_size = max(max_size,size+1)
        
        return max_size
                        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
