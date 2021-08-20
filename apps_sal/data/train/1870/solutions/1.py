class Solution:

    def sampleStats(self, count: List[int]) -> List[float]:
        N = sum(count)
        total = 0
        c = 0
        median = pre = post = -1
        mm = 256
        MM = -1
        mode = (-1, -1)
        for i in range(len(count)):
            total += count[i] * i
            c += count[i]
            if count[i]:
                mm = min(mm, i)
                MM = max(MM, i)
                mode = max(mode, (count[i], i))
            if median < 0:
                if c >= N / 2:
                    if N % 2:
                        pre = post = i
                    elif c == N / 2:
                        pre = i
                    elif pre > 0:
                        post = i
                    else:
                        pre = post = i
                if pre > 0 and post > 0:
                    median = (pre + post) / 2
        mean = total / N
        return [mm, MM, mean, median, mode[1]]
