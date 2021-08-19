class Solution:

    def sampleStats(self, count: List[int]) -> List[float]:
        ans = []
        for i in range(0, len(count)):
            if count[i] != 0:
                ans.append(i)
                break
        for i in range(len(count) - 1, 0, -1):
            if count[i] != 0:
                ans.append(i)
                break
        s = 0
        for i in range(0, len(count)):
            s += i * count[i]
        total = sum(count)
        ans.append(s / total)
        total = sum(count)
        if total % 2 == 0:
            total = total // 2
            for i in range(0, len(count)):
                total = total - count[i]
                if total == 0:
                    med = (i + i + 1) / 2
                    ans.append(med)
                    break
                if total < 0:
                    med = i
                    ans.append(med)
                    break
        else:
            total = total // 2
            for i in range(0, len(count)):
                total = total - count[i]
                if total <= 0:
                    med = i
                    ans.append(med)
                    break
        ans.append(max(range(len(count)), key=count.__getitem__))
        return ans
