class Solution:
    def arrangeWords(self, text: str) -> str:
        p = text.split(' ')
        final = ''
        j = sorted(p, key=len)
        temp = ' '.join(j)
        if temp[0] >= 'a' and temp[0] <= 'z':
            s = temp[0].swapcase()
            final = final + s[0]
        else:
            final = final + temp[0]
        for i in range(1, len(temp)):
            if temp[i] >= 'A' and temp[i] <= 'Z':
                s = temp[i].swapcase()
                final = final + s[0]
            else:
                final = final + temp[i]
        return final
