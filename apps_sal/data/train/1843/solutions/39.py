class TweetCounts:
    def __init__(self):
        self.tweets = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweets:
            self.tweets[tweetName] = []
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == \"minute\":
            delta = 60
        elif freq == \"hour\":
            delta = 60*60
        else:
            delta = 60*60*24
            
        result = [0] * (((endTime - startTime) // delta) + 1)
        for tweetTime in self.tweets[tweetName]:
            if startTime <= tweetTime <= endTime:
                result[((tweetTime - startTime) // delta)] += 1
        return result

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
