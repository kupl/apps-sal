class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def visit(a, depth):     
            if a in depths:
                return (depth - depths[a]) % 2 == 0

            depths[a] = depth
            return all(visit(b, depth + 1) for b in d[a])

        d = collections.defaultdict(set)
        depths = {}
        for a,b in dislikes:
            d[a].add(b)
            d[b].add(a)

        return all(a in depths or visit(a, 0) for a in d)
            

