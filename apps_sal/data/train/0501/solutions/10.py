class Solution:
    def shortestPalindrome(self, s):
        rev = s[::-1]
        aux = s + '#' + rev
        num = self.getNextArray(aux)
        return rev[:-num] + s

    def getNextArray(self, seq):
        length = len(seq)
        nextarray = [0] * length
        nextarray[0] = 0
        pos = 1
        cn = 0
        while pos < length:
            if seq[pos] == seq[cn]:
                cn += 1
                nextarray[pos] = cn
                pos += 1
            else:
                if cn > 0:
                    cn = nextarray[cn - 1]
                else:
                    nextarray[pos] = 0
                    pos += 1
        return nextarray[-1]
