class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        chars_number = collections.Counter(chars)
        for w in words:
            word_number = collections.Counter(w)
            print(word_number)
            for i in word_number:
                print(word_number[i])
                if word_number[i] > chars_number[i]:

                    break
            else:
                ans += len(w)
        return ans
