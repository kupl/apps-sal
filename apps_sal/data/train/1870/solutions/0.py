class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        mn = -1
        mx = 0
        sm = 0
        cnt = 0
        mode_i = 0
        mode_cnt = 0
        indexes = collections.deque()
        median_count = 0

        for i, c in enumerate(count):
            sm += i * c
            cnt += c

            mode_i = i if mode_cnt < c else mode_i
            mode_cnt = c if mode_cnt < c else mode_cnt

            if c:
                mx = i
                if mn == -1:
                    mn = i
                while indexes and median_count + count[indexes[0]] < cnt / 2:
                    median_count += count[indexes[0]]
                    indexes.popleft()
                indexes.append(i)

        median = 0

        if cnt % 2:
            median = indexes[0]
        elif count[indexes[0]] + median_count > cnt // 2:
            median = indexes[0]
        else:
            median = (indexes[0] + indexes[1]) / 2

        return mn, mx, sm / cnt, median, mode_i
