class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        good_words_len_sum = 0
        counter = {}
        for char in chars:
            if not char in counter:
                counter[char] = 1
            else:
                counter[char] += 1
        for word in words:
            my_counter = counter.copy()
            for char in word:
                if my_counter.get(char, 0) > 0:
                    my_counter[char] -= 1
                else:
                    break
            else:
                good_words_len_sum += len(word)
        return good_words_len_sum
