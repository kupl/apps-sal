class Solution:

    def get_num(self, S, i, j, cache):
        if i == j:
            return int(S[i])
        key = '{}-{}'.format(i, j)
        if key in cache:
            return cache[key]
        v = int(S[i:j + 1])
        cache[key] = v
        return v

    def check(self, st, v):
        if v > 2 ** 31 - 1:
            return False
        if len(st) < 2:
            return True
        return st[-2] + st[-1] == v

    def get_st_key(self, st):
        k1 = None
        k2 = None
        ln = len(st)
        if ln == 0:
            pass
        elif ln == 1:
            k1 = st[-1]
        else:
            k1 = st[-1]
            k2 = st[-2]
            if k1 > k2:
                (k1, k2) = (k2, k1)
        return '{}-{}'.format(k1, k2)

    def split(self, S, i, st, res, cache, cache_res):
        ln = len(S)
        if i >= ln:
            if len(st) >= 3:
                res[0] = list(st)
                return True
            return False
        key = self.get_st_key(st)
        if key in cache_res:
            return cache_res[key]
        res_local = False
        if S[i] == '0':
            new_v = 0
            if self.check(st, new_v):
                st.append(new_v)
                res_local = self.split(S, i + 1, st, res, cache, cache_res)
                del st[-1]
        else:
            for j in range(i, len(S)):
                new_v = self.get_num(S, i, j, cache)
                if self.check(st, new_v):
                    st.append(new_v)
                    res_local = self.split(S, j + 1, st, res, cache, cache_res)
                    del st[-1]
                    if res_local:
                        break
                if len(st) >= 2 and new_v > st[-2] + st[-1]:
                    break
        cache_res[key] = res_local
        return res_local

    def solve(self, S):
        res = [None]
        self.split(S, 0, [], res, {}, {})
        if res[0] is None:
            return []
        return res[0]

    def splitIntoFibonacci(self, S: str) -> List[int]:
        return self.solve(S)
