class Solution:
    tree = []
    n = 0
    def SegmentTree(self, arr):
        nonlocal tree, n
        n = len(arr)
        tree = [0]*2*n
        for i in range(n):
            tree[i+n] = arr[i]
        for j in range(n-1, 0, -1):
            tree[j] = tree[2 * j] ^ tree[2 * j + 1]
        #print(tree)
    def xor(self, frm, to):
        nonlocal tree, n
        frm += n
        to += n
        value = 0
        while(frm < to):
            if(frm & 1 == 1):
                value ^= tree[frm]
                frm += 1
            if(to & 1 == 1):
                to -= 1
                value ^= tree[to]
            frm >>= 1
            to >>= 1
        
        return value
            
        
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        self.SegmentTree(arr)
        result = []        
        for query in queries:
            #print(query[0], query[1]+1) DEBUG PRINT
            result.append(self.xor(query[0], query[1]+1))

        return result

