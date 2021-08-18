class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        '''
         size = len(S)
         limit = size//2 + size%2
         cnt = collections.Counter(S)
         res = [0]*size
         i = 0
         for k, v in cnt.most_common():
             if v > limit:
                 return ''
             for _ in range(v):
                 if i >= size:
                     i = res.index(0)
                 res[i] = k
                 i += 2
         return ''.join(res)
         '''
        cnt = collections.Counter(S)
        res = '
        while cnt:
            stop = True
            for k, v in cnt.most_common():
                if k != res[-1]:
                    stop = False
                    res += k
                    cnt[k] -= 1
                    if not cnt[k]:
                        del cnt[k]
                    break
            if stop == True:
                break
        return res[1:] if len(res) == len(S) + 1 else ''
