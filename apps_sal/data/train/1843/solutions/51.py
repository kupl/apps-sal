class TweetCounts:
    deltaDic = {'minute': 60, 'hour': 3600, 'day': 24 * 3600}

    def __init__(self):
        self.tweetDic = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if not tweetName in self.tweetDic:
            self.tweetDic[tweetName] = []
        self.tweetDic[tweetName].append(time)
        self.tweetDic[tweetName].sort()

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if not tweetName in self.tweetDic:
            return []
        delta = self.deltaDic[freq]
        output = [0] * ((endTime - startTime) // delta + 1)
        for t in self.tweetDic[tweetName]:
            if t < startTime:
                continue
            elif t > endTime:
                continue
            else:
                idx = (t - startTime) // delta
                output[idx] += 1
        return output
