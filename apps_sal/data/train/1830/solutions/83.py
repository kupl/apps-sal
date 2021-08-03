class Solution(object):
    def avoidFlood(self, rains):
        aux = dict()
        for i in range(len(rains)):
            if rains[i] not in aux:
                aux[rains[i]] = deque()
            aux[rains[i]].append(i)
        q = []
        ans = [1] * len(rains)
        for i in range(len(rains)):
            if rains[i] == 0:
                if q:
                    index, val = heapq.heappop(q)
                    if index < i:
                        return []
                    else:
                        ans[i] = val
            else:
                ans[i] = -1
                if len(aux[rains[i]]) > 1:
                    aux[rains[i]].popleft()
                    heapq.heappush(q, (aux[rains[i]][0], rains[i]))
        if len(q):
            return []
        return ans
