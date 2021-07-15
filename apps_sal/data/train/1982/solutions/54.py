class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes: return True
        
        v = collections.defaultdict(int)
        for a, b in dislikes:
            v[a] += 1
            v[b] += 1
        
        d = []
        for a, b in dislikes:
            if v[a] == 1 and v[b] == 1:
                continue
            d.append([a, b])
            
        d.sort(key = lambda x:x[0])
        c1, c2 = set(), set()
        c1.add(d[0][0])
        c2.add(d[0][1])
        for a, b in d[1:]:
            if (a in c1 and b in c1) or (a in c2 and b in c2):
                return False
            if a in c1:
                c2.add(b)
            elif a in c2:
                c1.add(b)
        return True
