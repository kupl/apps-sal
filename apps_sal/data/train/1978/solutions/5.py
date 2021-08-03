class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def encodeWord(word):
            d, nextChar, i, encoding = {}, iter([chr(ord('a') + i) for i in range(26)]), 0, []

            while i < len(word):
                c, count = word[i], 1
                while i + 1 < len(word) and word[i + 1] == c:
                    i, count = i + 1, count + 1
                if c not in d:
                    d[c] = next(nextChar)
                encoding.append(d[c] + str(count))
                i += 1
            return ''.join(encoding)

        p_enc = encodeWord(pattern)
        # print(p_enc)
        return [word for word in words if encodeWord(word) == p_enc]
