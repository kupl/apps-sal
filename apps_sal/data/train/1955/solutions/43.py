import collections
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.uf_table = [idx for idx in range(len(s))]
        def find(p):
            if p != self.uf_table[p]:
                self.uf_table[p] = find(self.uf_table[p])
            return self.uf_table[p]
        
        for p, q in pairs:
            rp = find(p)
            rq = find(q)
            if rp != rq:
                self.uf_table[rp] = rq
                
        conn = collections.defaultdict(list)
        for idx, p in enumerate(self.uf_table):
            conn[find(p)].append(s[idx])
        for k, v in conn.items():
            conn[k] = sorted(v)
        result = []
        for idx in range(len(s)):
            result.append(conn[find(idx)].pop(0))
        
        return ''.join(result)
