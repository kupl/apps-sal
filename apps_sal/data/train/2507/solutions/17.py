class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        suma = 0
        for word in words:
            cur_word = list(word)
            cur_len = len(word)
            for c in chars:
                if c in cur_word:
                    cur_word.remove(c)
            if len(cur_word) == 0:
                suma += cur_len
        return suma
