class TweetCounts:

    def __init__(self):
        self.memo = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.memo[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        lst = self.memo[tweetName]
        lst = [t - startTime for t in lst if t >= startTime and t <= endTime]
        if freq == 'minute':
            freq = 60
        elif freq == 'hour':
            freq = 60 * 60
        elif freq == 'day':
            freq = 24 * 60 * 60
        length, remainder = divmod(endTime - startTime + 1, freq)
        if remainder > 0:
            length += 1
        res = [0 for _ in range(length)]
        for t in lst:
            res[t // freq] += 1
        return res
