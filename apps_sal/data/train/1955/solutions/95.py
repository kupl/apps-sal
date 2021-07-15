class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        l = len(s)
        union_find = [i for i in range(l)]
        union_set = {}
        for i in range(l):
            union_set[i] = [i]
        for p in pairs:
            x = p[0]
            y = p[1]
            t, t1 = union_find[y], union_find[x]
            if union_find[x] < union_find[y]:
                t, t1 = union_find[x], union_find[y]
            if t == t1:
                continue
            for i in union_set[t1]:
                union_set[t].append(i)
                union_find[i] = t
            union_set[t1] = []
        print(union_find)
        print(union_set)
        res_cand = {}
        for k, v in list(union_set.items()):
            union_set = []
            for i in v:
                union_set.append(s[i])
            union_set.sort(reverse=True)
            res_cand[k] = union_set

        print(res_cand)
        res = ''
        for i in range(l):
            res = res + res_cand[union_find[i]][-1]
            res_cand[union_find[i]].pop()
        return res

