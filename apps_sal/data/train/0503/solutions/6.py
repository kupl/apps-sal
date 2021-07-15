class Solution:
    def arrangeWords(self, text: str) -> str:
        dic = collections.OrderedDict()
        for word in text.split():
            n = len(word)
            dic[n] = dic.get(n, []) + [word.lower()]

        res = []
        for key, val in sorted(dic.items()):
            res += val

        return ' '.join(res).capitalize()
