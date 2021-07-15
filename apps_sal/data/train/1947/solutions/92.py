class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        min_require = [0]*26
        std_string = \"abcdefghijklmnopqrstuvwxyz\"
        for word in B:
            curr_char_freq = [0]*26
            for char in word:
                curr_char_freq[std_string.index(char)] += 1
            
            min_require = [max(x1, x2) for x1,x2 in zip(min_require, curr_char_freq)]
        
        result = []
        for word in A:
            curr_char_freq = [0]*26
            for char in word:
                curr_char_freq[std_string.index(char)] += 1
            
            if False in [curr_char_freq[i] >= min_require[i] for i in range(26)]:
                continue
            result.append(word)
        return result
