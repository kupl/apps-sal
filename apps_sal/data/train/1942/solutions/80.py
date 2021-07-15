class UnionFind:
    
    def __init__(self, favorites):
        self.n = len(favorites)
        self.arr = list(range(self.n))
        self.favorites = [set(x) for x in favorites]
        
    def union(self, a, b):
        \"\"\"Returns true if you can end search early, else False.\"\"\"
        a, b = self.find(a), self.find(b)
        if a == b:
            return True
        
        a_fav, b_fav = self.favorites[a], self.favorites[b]
        if a_fav.issubset(b_fav):
            self.arr[a] = b
            return True
        if b_fav.issubset(a_fav):
            self.arr[b] = a
            return True
        
        return False
        
    def find(self, a):
        head = a
        while self.arr[head] != head:
            head = self.arr[head]
            
        # path compression
        ptr = a
        while a != head:
            a = self.arr[a]
            self.arr[ptr] = head
            ptr = a
        
        return head
        
    def num_groups(self):
        return [i for i in range(self.n) if self.arr[i] == i]

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        \"\"\"
        API
        count_num_groups (head of each group will be people without subsets)
        union (if in same group, do nothing. If a is subset of b, a points to b.)
        \"\"\"
        uf = UnionFind(favoriteCompanies)
        n = len(favoriteCompanies)
        for i in range(n):
            for j in range(i + 1, n):
                if uf.union(i, j):
                    break
        return uf.num_groups()
        
