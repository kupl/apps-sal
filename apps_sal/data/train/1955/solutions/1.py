class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        
        parents = [i for i in range(n)]

        def find_parent(i):
            while parents[i] != i:
                # path compression
                parents[i] = parents[parents[i]]
                i = parents[i]
            return i

        def do_union(p, q):
            i = find_parent(p)
            j = find_parent(q)
            parents[i] = j

        for p, q in pairs:
            do_union(p, q)
       
        groups = defaultdict(list)
        for i in range(len(s)):
            root = find_parent(i)
            groups[root].append(i)
        
        s = list(s)
        for indices in sorted(groups.values()):
            vals = sorted([s[i] for i in indices])
            for i, c in enumerate(vals):
                s[indices[i]] = c
            
        return ''.join(s)
