class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        uni = []
        B_set = set(''.join(B))
        B_hist = {b_i: [max([b.count(b_i) for b in B]), -1] for b_i in B_set}
        for a in A:
            occurances_b = 0
            for b_i in B_set:
                occurances_b_i = 0
                stop = False
                B_hist[b_i][1] = -1
                for j in range(B_hist[b_i][0]):
                    B_hist[b_i][1] = a.find(b_i, B_hist[b_i][1] + 1)
                    if B_hist[b_i][1] == -1:
                        stop = True
                        break
                    else:
                        occurances_b_i += 1
                if stop == True:
                    break
                if occurances_b_i == B_hist[b_i][0]:
                    occurances_b += 1
            if occurances_b == len(B_set):
                uni.append(a)
        return uni
