from collections import defaultdict
class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)
        
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        tweet_ts = self.tweets[tweetName]
        if not len(tweet_ts):
            return []
        diff = endTime - startTime
        seconds_in_interval = 0
        if freq == \"minute\":
            seconds_in_interval = 60
        elif freq == \"hour\":
            seconds_in_interval = 3600
        else:
            seconds_in_interval = 3600 * 24
        output = [0] * ((diff//seconds_in_interval) + 1)
        for ts in tweet_ts:
            if endTime >= ts >= startTime:
                output[(ts - startTime)//seconds_in_interval] += 1
        return output
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
