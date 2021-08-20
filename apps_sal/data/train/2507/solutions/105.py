class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        tot = 0
        totchars = {}
        for char in chars:
            if char in totchars:
                totchars[char] += 1
            else:
                totchars[char] = 1
        for word in words:
            word = sorted(word)
            works = True
            i = 0
            while i < len(word):
                count = 0
                while word[i + count] == word[i]:
                    count += 1
                    if i + count == len(word):
                        break
                if word[i] in totchars:
                    if count > totchars[word[i]]:
                        works = False
                else:
                    works = False
                i += count
            if works:
                tot += len(word)
        return tot
