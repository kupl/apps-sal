class TweetCounts:

    def __init__(self):
        self.tweets = collections.defaultdict(list)

    def __bs(self, arr, val):
        (lo, hi) = (0, len(arr))
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] >= val:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def recordTweet(self, tweetName: str, time: int) -> None:
        idx = self.__bs(self.tweets[tweetName], time)
        self.tweets[tweetName].insert(idx, time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        i = startTime
        arr = self.tweets[tweetName]
        result = []
        while i <= endTime:
            j = min(i + delta, endTime + 1)
            result.append(self.__bs(arr, j) - self.__bs(arr, i))
            i += delta
        return result
