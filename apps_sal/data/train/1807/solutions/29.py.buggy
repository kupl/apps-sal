class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for i in range(2, n + 1) :
            for j in range(1, i) :
                if not ((i % 2 == 0) and (j % 2 == 0)) :
                    res_flag = True
                    for k in range(3, j + 1, 2):
                        if (i % k == 0) and (j % k == 0) :
                            res_flag = False
                            break
                    if res_flag : res.append(str(j) + \"/\" + str(i))
        return res
