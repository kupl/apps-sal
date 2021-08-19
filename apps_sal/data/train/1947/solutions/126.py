class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        max_count = {}
        for string in B:
            char_count = {}
            for ch in string:
                char_count[ch] = char_count.get(ch, 0) + 1
            for ch in char_count:
                if ch not in max_count:
                    max_count[ch] = 0
                max_count[ch] = max(max_count[ch], char_count[ch])
        print(max_count)
        res = []
        for string in A:
            char_count = {}
            for ch in string:
                char_count[ch] = char_count.get(ch, 0) + 1
            uni = True
            for key in max_count:
                if key not in char_count or max_count[key] > char_count[key]:
                    uni = False
                    break
            if uni:
                res.append(string)
        return res
