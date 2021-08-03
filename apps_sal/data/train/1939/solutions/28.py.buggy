class Solution:
    def spellchecker(self, w: List[str], q: List[str]) -> List[str]:
        s = {i for i in w}
        d = {w[i].lower(): i for i in range(len(w)-1, -1, -1)}
        vowel = [\"a\", \"e\", \"i\", \"o\", \"u\"]
        # print(d, s)
        ans = []
        def func(i):
            n = len(i)
            # print(n, i)
            ls = [\"\"]
            ind = float(\"inf\")
            for j in range(n):
                if i[j] in vowel:
                    ls = [item+vow for item in ls for vow in vowel]
                else:
                    ls = [item+i[j] for item in ls]
            # print(i, ls)
            for item in ls:
                if item in d:
                    ind = min(ind, d[item])
                if ind == 0:
                    return ind
            return ind
        for i in q:
            if i in s:
                ans.append(i)
                continue
            i = i.lower()
            if i in d:
                ans.append(w[d[i]])
                continue
            flag = func(i)
            # print(flag)
            if flag == float(\"inf\"):
                ans.append(\"\")
            else:
                ans.append(w[flag])
        return ans
