class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        edges = collections.defaultdict(list)
        for p in pairs:
            edges[p[0]].append(p[1])
            edges[p[1]].append(p[0])
            
        # print(edges)
        
        ans = list(s)
        seen = set()
        for i,c in enumerate(s):
            if i in seen: continue
            seen.add(i)
            h1,h2 = [],[]
            frontier = [i]
            while frontier:
                cur = frontier.pop()
                heapq.heappush(h1,cur)
                heapq.heappush(h2,ans[cur])
                for j in edges[cur]:
                    # print(cur,j)
                    if j not in seen:
                        # print('New index')
                        seen.add(j)
                        frontier.append(j)
            # print(f' Current-{cur}, h1-{h1}, h2-{h2}')
            while h1: ans[heapq.heappop(h1)] = heapq.heappop(h2)
        
        return ''.join(ans)
