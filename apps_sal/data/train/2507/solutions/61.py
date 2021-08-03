class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        def get_freq(input):
            freq = {}
            for c in input:
                if c not in freq:
                    freq[c] = 0
                freq[c] += 1
            return freq

        def can_contain(freq_source, freq_word):
            for key, item in freq_word.items():
                if key not in freq_source or freq_source[key] < item:
                    return False

            return True

        total_length = 0
        freq_source = get_freq(chars)
        for word in words:
            freq_word = get_freq(word)
            if can_contain(freq_source, freq_word):
                total_length += len(word)

        return total_length
