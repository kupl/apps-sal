import copy
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parent = [0]*n
        ans = 0
        alice = 0
        bob = 0

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[py] = px
            return True
        
        #both
        for i in range(n):
            parent[i] = i
            
        for i in range(len(edges)):
            t, u, v = edges[i]
            if t == 3:
                if union(u-1,v-1):
                    alice += 1
                    bob += 1
                else:
                    ans += 1
                    
        #alice
        ogparent = copy.deepcopy(parent)
        for i in range(len(edges)):
            t, u, v = edges[i]
            if t == 1:
                if union(u-1,v-1):
                    alice += 1
                else:
                    ans += 1
        for i in range(n):
            parent[i] = i
        #bob
        parent = copy.deepcopy(ogparent)
        for i in range(len(edges)):
            t, u, v = edges[i]
            if t == 2:
                if union(u-1, v-1):
                    bob += 1
                else:
                    ans += 1
        print((alice, bob, ans))
        if alice == n-1 and bob == n-1:
            return ans
        return -1
                

