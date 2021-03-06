class Solution:

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        vis = {id}
        q = deque()
        q.append(id)
        while q and level:
            ln = len(q)
            for _ in range(ln):
                x = q.popleft()
                for i in friends[x]:
                    if i not in vis:
                        q.append(i)
                        vis.add(i)
            level -= 1
        d = defaultdict(int)
        for i in q:
            for j in watchedVideos[i]:
                d[j] += 1
        'd2=defaultdict(list)\n        for i in d:\n            d2[d[i]].append(i)\n        for i in d2: d2[i].sort()\n        x=sorted(list(d2.keys()))\n        res=[]\n        for i in x: \n            for j in d2[i]: res.append(j)\n        return res'
        pq = []
        res = []
        for i in d:
            heapq.heappush(pq, (d[i], i))
        while pq:
            res.append(heapq.heappop(pq)[1])
        return res
