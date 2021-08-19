class Solution:

    def getFolderNames(self, lis: List[str]) -> List[str]:
        s = set()
        ans = []
        d = {}
        for i in lis:
            if i in s:
                k = d[i]
                while 1 > 0:
                    tmp = '%s(%d)' % (i, k)
                    if tmp in s:
                        k += 1
                    else:
                        break
                d[i] = k
                d['%s(%d)' % (i, k)] = 1
                s.add('%s(%d)' % (i, k))
                ans.append('%s(%d)' % (i, k))
            else:
                d[i] = 1
                s.add(i)
                ans.append(i)
        return ans
