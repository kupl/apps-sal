class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter = collections.Counter(S)
        h = [(-v, k) for k, v in list(counter.items())]
        heapq.heapify(h)
        ans = []
        while h:
            v, c = heapq.heappop(h)
            ans.append(c)
            counter[c] -= 1
            if len(ans) >= 2:
                ch = ans[-2]
                if counter[ch] > 0:
                    heapq.heappush(h, (-counter[ch], ch))
        if len(ans) < len(S):
            return ""
        return ''.join(ans)
