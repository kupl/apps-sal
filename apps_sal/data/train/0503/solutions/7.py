class Solution:

    def arrangeWords(self, text: str) -> str:
        dic = collections.OrderedDict()
        for word in text.split():
            dic[len(word)] = dic.get(len(word), []) + [word.lower()]
        res = []
        for (key, val) in sorted(dic.items()):
            res += val
        res = [res[0].capitalize()] + res[1:]
        return ' '.join(res)
