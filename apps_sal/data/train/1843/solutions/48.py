class TweetCounts:

    def __init__(self):
        self.tweets = collections.defaultdict(list)
        self.convert = {'minute': 60, 'hour': 3600, 'day': 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        ans = [0] * ((endTime - startTime) // self.convert[freq] + 1)
        for t in self.tweets[tweetName]:
            if startTime <= t <= endTime:
                ans[(t - startTime) // self.convert[freq]] += 1
        return ans
