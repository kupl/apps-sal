class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        seen = set()
        freq_B = [0] * 26
        for word in B:
            if word not in seen:
                seen.add(word)

                freq_cur = [0] * 26
                for c in word:
                    freq_cur[ord(c) - ord('a')] += 1

                for i in range(26):
                    freq_B[i] = max(freq_B[i], freq_cur[i])

        ans = []
        for word in A:
            freq_A = [0] * 26
            for c in word:
                freq_A[ord(c) - ord('a')] += 1

            broke_early = False
            for i in range(26):
                if freq_A[i] < freq_B[i]:
                    broke_early = True
                    break
            if broke_early:
                continue
            ans += [word]
        return ans
