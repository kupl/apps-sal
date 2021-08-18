class TweetCounts:

    def __init__(self):
        self.store = defaultdict(list)
        self.delta = {'hour': 3600, 'minute': 60, 'day': 24 * 3600}

    def recordTweet(self, tn: str, time: int) -> None:
        insort(self.store[tn], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        d = self.delta[freq]
        ans = []
        arr = self.store[tweetName]

        for st_time in range(startTime, endTime + 1, d):
            left = bisect_left(arr, st_time)
            right = bisect_right(arr, min(endTime, st_time + d - 1)) - 1

            ans.append(min(right - left + 1, len(arr)))

        return ans
