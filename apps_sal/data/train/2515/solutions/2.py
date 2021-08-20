class Solution:

    def toGoatLatin(self, S: str) -> str:
        words = S.split(' ')

        def trans(word):
            ret = ''
            if word[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                ret = word + 'ma'
            else:
                ret = word[1:] + word[0] + 'ma'
            return ret
        ret = [trans(x) for x in words]
        for idx in range(len(ret)):
            ret[idx] += 'a' * (idx + 1)
        return ' '.join(ret)
