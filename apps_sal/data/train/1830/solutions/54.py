class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        q = []  # list for zeros positions
        ans = []
        hashmap = {}
        for i in range(len(rains)):
            if rains[i] == 0:
                q.append(i)
                ans.append(1)  # as per example 4
            else:
                if rains[i] in hashmap:
                    if len(q) == 0:
                        return []
                    else:
                        index = hashmap[rains[i]]
                        # find a zero position just greater than previous occurrence of rains[i]
                        pos = bisect.bisect_right(q, index)
                        if pos < len(q):  # no zero exists in between occurrence
                            ans[q[pos]] = rains[i]
                            q.pop(pos)
                        else:
                            return []
                hashmap[rains[i]] = i
                ans.append(-1)

        return ans
