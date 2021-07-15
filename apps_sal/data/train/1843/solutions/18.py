class TweetCounts:

    def __init__(self):
        self.tweets = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweets:
            self.tweets[tweetName] = []
        left, right = 0, len(self.tweets[tweetName])
        while left < right:
            mid = left + (right-left)//2
            if self.tweets[tweetName][mid]>=time:
                right = mid
            else:
                left = mid+1
        self.tweets[tweetName].insert(left, time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = {\"minute\": 60, \"hour\": 60*60, \"day\": 60*60*24}
        interval = delta[freq]
        num_intervals = (endTime - startTime) // interval + 1
        count = [0] * num_intervals
        for t in self.tweets[tweetName]:
            if t<startTime:
                continue
            if t>endTime:
                break
            count[(t - startTime) // interval]+=1
        return count


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
