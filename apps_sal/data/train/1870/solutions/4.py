class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        d = {}
        mini = None
        sample_size = total = 0
        mode = (-1, -1)
        for n, freq in enumerate(count):
            if freq:
                maxi = n
                if mini is None:
                    mini = n
                sample_size += freq
                total += n * freq
                d[sample_size] = n
            if freq > mode[1]:
                mode = (n, freq)
        d = {k:v for k, v in d.items() if k >= sample_size / 2}
        median = d[min(d)]
        if sample_size % 2 == 0 and sample_size / 2 in d:
            del d[min(d)]
            median += d[min(d)]
            median /= 2
        return [mini, maxi, total/sample_size, median, mode[0]]
