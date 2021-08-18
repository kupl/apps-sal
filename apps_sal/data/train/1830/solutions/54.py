class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        q = []
        ans = []
        hashmap = {}
        for i in range(len(rains)):
            if rains[i] == 0:
                q.append(i)
                ans.append(1)
            else:
                if rains[i] in hashmap:
                    if len(q) == 0:
                        return []
                    else:
                        index = hashmap[rains[i]]
                        pos = bisect.bisect_right(q, index)
                        if pos < len(q):
                            ans[q[pos]] = rains[i]
                            q.pop(pos)
                        else:
                            return []
                hashmap[rains[i]] = i
                ans.append(-1)

        return ans
