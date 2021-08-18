class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        mini = -1
        maxi = 0.0
        mode = 0.0
        biggest = 0
        total = sum(count)
        mid = total // 2 if total != 1 else 1
        median = 0.0
        accumulator = 0
        tally = 0
        nums = 0

        for i, num in enumerate(count):
            if not num:
                continue
            else:
                maxi = float(i)
                tally += num * i

            if mini == -1 and num:
                mini = float(i)
            if num > biggest:
                biggest = num
                mode = float(i)

            if total % 2:
                if accumulator < mid and (accumulator + num) >= mid:
                    median = float(i)
            else:
                if accumulator < mid - 1 and (accumulator + num) >= mid - 1:
                    median = float(i)
                elif num and accumulator == mid:
                    median = (median + i) / 2
            accumulator += num
        return [mini, maxi, tally / accumulator, median, mode]
