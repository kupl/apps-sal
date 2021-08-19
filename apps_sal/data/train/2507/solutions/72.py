class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        freq = {}
        for n in range(len(chars)):
            if chars[n] not in freq.keys():
                freq[chars[n]] = 1
            else:
                freq[chars[n]] += 1
        for word in words:
            word_fq = {}
            for m in range(len(word)):
                if word[m] not in word_fq.keys():
                    word_fq[word[m]] = 1
                else:
                    word_fq[word[m]] += 1
            is_fit = True
            for key in word_fq.keys():
                if key not in freq.keys():
                    is_fit = False
                    break
                if word_fq[key] > freq[key]:
                    is_fit = False
                    break
            if is_fit:
                count += len(word)
        return count
