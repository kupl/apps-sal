from collections import Counter


class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        c_dict = dict(Counter(chars))
        count = 0
        for word in words:
            word_d = dict(Counter(word))
            match = True
            for (k, v) in list(word_d.items()):
                if k not in c_dict or v > c_dict[k]:
                    match = False
                    break
            if match:
                count += len(word)
        return count
