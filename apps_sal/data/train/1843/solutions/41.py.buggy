class TweetCounts:

    def __init__(self):
        self.tweets = {}
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets.setdefault(tweetName, []).append(time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == \"minute\":
            seconds = 60
        elif freq == \"hour\":
            seconds = 3600
        else:
            seconds = 86400
        rep = (endTime-startTime)//seconds+1
        ans = [0 for _ in range(rep)]
        for tweet_time in self.tweets[tweetName]:
            if startTime<=tweet_time<=endTime:
                ans[(tweet_time-startTime)//seconds]+=1
        return ans


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
