class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        dic_char = {}
        for i in chars:
            if i not in dic_char:
                dic_char[i] = 1
            else:
                dic_char[i] += 1
        cnt = 0
        for i in words:
            dic_word = {}
            for j in i:
                if j not in dic_word:
                    dic_word[j] = 1
                else:
                    dic_word[j] += 1
            print(dic_word)
            for (k, v) in dic_word.items():
                if k not in dic_char or dic_char[k] < v:
                    break
            else:
                cnt += len(i)
        return cnt
