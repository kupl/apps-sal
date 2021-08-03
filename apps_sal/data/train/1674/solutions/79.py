class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        M = (len(piles) + 1) // 2
        record = [[0 for _ in range(len(piles))] for _ in range(M)]
        total = [0 for _ in range(len(piles))]
        for i in range(M):
            record[i][-1] = piles[-1]
        total[-1] = piles[-1]

        for i in range(len(piles) - 2, -1, -1):
            total[i] = total[i + 1] + piles[i]

        for i in range(len(piles) - 2, -1, -1):
            for j in range(M):
                min_num = float(inf)
                for k in range(2 * (j + 1)):
                    if i + k + 1 >= len(piles):
                        if min_num > 0:
                            min_num = 0
                    else:
                        if record[min(max(j, k), M - 1)][i + k + 1] < min_num:
                            min_num = record[min(max(j, k), M - 1)][i + k + 1]

                record[j][i] = total[i] - min_num
        print(record)
        return record[0][0]
