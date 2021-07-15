class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def get_b_map(words):
            res = collections.defaultdict(int)
            for word in words:
                temp_dict = collections.defaultdict(int)
                for char in word:
                    temp_dict[char] += 1
                    res[char] = max(res[char], temp_dict[char])
            return res
        
        b_map = get_b_map(B)
        
        def contains(word, b_map):
            same_freqs = 0
            temp_dict = collections.defaultdict(int)
            for char in word:
                if char not in b_map:
                    continue
                    
                temp_dict[char] += 1
                if temp_dict[char] == b_map[char]:
                    same_freqs += 1
            return same_freqs == len(b_map)
        
        res = []
        for word in A:
            if contains(word, b_map):
                res.append(word)
        return res
