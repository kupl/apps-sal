class Solution:
    def longestWord(self, words):
        ret, m = '', {''}
        for w in sorted(words):
            if w[:-1] in m:
                m.add(w)
                ret = max(ret, w, key=len)
        return ret
