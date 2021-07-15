class Solution(object):
    def pancakeSort(self, arr):
        p = arr.copy()
        final = p.copy()
        final.sort()
        print(p)
        k = len(final) - 1
        ret = []
        while k >= 0:
            val = final[k]
            print(\"value = \", val)
            ind = p.index(val)
            print(\"p array = \", p)
            print(\"index for\", val, \"=\", ind)
            if ind != k and ind != 0:
                p = p[:(ind+1)][::-1] + p[(ind+1):]
                p = p[:(k+1)][::-1] + p[(k+1):]
                ret += [ind+1, k+1]
            elif ind == k:
                pass
            elif ind == 0:
                p = p[:(k+1)][::-1] + p[(k+1):]
                ret.append(k+1)
            k -= 1
        return ret

