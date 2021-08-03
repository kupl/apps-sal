class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        d, ret = {}, []

        for word in B:

            b = Counter(word)

            for key, val in list(b.items()):

                if key not in d:
                    d[key] = val
                else:
                    d[key] = max(d[key], val)

        for cand in A:
            flag = True
            a = Counter(cand)

            for key, val in list(d.items()):

                if key not in a or val > a[key]:

                    flag = False

            if flag:
                ret.append(cand)

        return ret
