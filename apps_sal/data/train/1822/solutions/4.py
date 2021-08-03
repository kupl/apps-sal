class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        cnt = {i: words.count(i) for i in list(set(words))}
        cntRev = {}
        ans = []
        for key, val in cnt.items():
            if val not in cntRev:
                cntRev[val] = [key]
            else:
                cntRev[val].append(key)
        for num in sorted(cntRev, reverse=True):
            if k <= len(cntRev[num]):
                ans += sorted(cntRev[num])[:k]
                break
            else:
                ans += sorted(cntRev[num])
                k -= len(cntRev[num])
        return ans
