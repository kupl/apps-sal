class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distDict = defaultdict(dict)
        citySet = set(list(range(n)))
        visitedDict = defaultdict(dict)
        stack = []
        allEdge = 0
        for (a, b, w) in edges:
            distDict[a][b] = w
            distDict[b][a] = w
            allEdge += w
            if a in citySet:
                citySet.remove(a)
                heapq.heappush(stack, (-distanceThreshold, a, a))
                visitedDict[a][a] = distanceThreshold
            if b in citySet:
                citySet.remove(b)
                heapq.heappush(stack, (-distanceThreshold, b, b))
                visitedDict[b][b] = distanceThreshold
        if len(citySet) > 0:
            return max(citySet)
        if distanceThreshold > allEdge:
            return n - 1
        while stack:
            (dLeft, source, curr) = heapq.heappop(stack)
            dLeft *= -1
            for nextCity in distDict[curr]:
                if (nextCity not in visitedDict[source] or visitedDict[source][nextCity] < dLeft - distDict[curr][nextCity]) and distDict[curr][nextCity] <= dLeft:
                    visitedDict[source][nextCity] = dLeft - distDict[curr][nextCity]
                    heapq.heappush(stack, (-(dLeft - distDict[curr][nextCity]), source, nextCity))
        ansMax = float('inf')
        ans = -1
        for city in visitedDict:
            if ansMax > len(visitedDict[city]):
                ansMax = len(visitedDict[city])
                ans = city
            elif ansMax == len(visitedDict[city]):
                ans = max(ans, city)
        return ans
