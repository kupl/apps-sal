class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = collections.Counter(chars)
        good_str_len = 0
        for word in words:
            temp = char_count.copy()
            temp_str_len = 0
            for ch in word:
                if ch in temp and temp[ch] > 0:
                    temp_str_len += 1
                    temp[ch] -= 1
            if temp_str_len == len(word):
                good_str_len += len(word)
        return good_str_len
