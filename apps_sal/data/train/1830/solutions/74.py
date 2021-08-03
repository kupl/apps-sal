# https://blog.csdn.net/pfdvnah/article/details/106897444

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        sol = [53456 for _ in range(len(rains))]

        pos = collections.defaultdict(list)
        for idx, n in enumerate(rains):
            if n > 0:
                pos[n].append(idx)
        for key in pos:
            pos[key].reverse()

        q = []
        used = set()
        for idx, n in enumerate(rains):
            # print (q, used)
            if n > 0:
                if n in used:
                    return []
                else:
                    pos[n].pop()
                    if pos[n]:
                        heapq.heappush(q, (pos[n][-1], n))
                    else:
                        heapq.heappush(q, (math.inf, n))
                    used.add(n)
                sol[idx] = -1
            elif n == 0:
                if q:
                    _, val = heapq.heappop(q)
                    sol[idx] = val
                    used.remove(val)
        return sol
