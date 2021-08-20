class Solution:

    def arrangeWords(self, text: str) -> str:
        res = []
        res_t = ''
        for (idx, word) in enumerate(text.split()):
            res.append((len(word), idx, word.lower()))
        res.sort()
        for (l, _, word) in res:
            if res_t == '':
                res_t += word[0].upper() + word[1:]
            else:
                res_t += ' ' + word
        return res_t
