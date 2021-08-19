class Solution:

    def sampleStats(self, count: List[int]) -> List[float]:
        Min = len(count)
        Max = 0
        Sum = 0
        Num = 0
        curr_count = count[0]
        for i in range(len(count)):
            if count[i] != 0:
                Min = min(i, Min)
                Max = max(i, Max)
                Sum += i * count[i]
                Num += count[i]
                Mean = Sum / Num
                if count[i] > curr_count:
                    curr_count = count[i]
                    Mod = i * 1.0
        total = Num // 2
        if Num % 2 == 0:
            for i in range(Min, Max + 1):
                total = total - count[i]
                if total == 0:
                    Med = (2 * i + 1) / 2
                    break
                if total < 0:
                    Med = i
                    break
        else:
            for i in range(Min, Max + 1):
                total = total - count[i]
                if total <= 0:
                    Med = i
                    break
        return [float(Min), float(Max), Mean, Med, Mod]
