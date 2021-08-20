class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        from collections import Counter
        freq = {word: Counter(word) for word in A}
        queries = {word: Counter(word) for word in B}
        query = {chr(i): max((queries[word].get(chr(i), 0) for word in queries)) for i in range(ord('a'), ord('z') + 1)}
        ans = []
        for k in list(freq.keys()):
            flag = 1
            for ch in query:
                if query[ch] > freq[k].get(ch, 0):
                    flag = 0
                    break
            if flag:
                ans.append(k)
        return ans
