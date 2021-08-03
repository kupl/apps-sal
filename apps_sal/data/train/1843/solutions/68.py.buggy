class TweetCounts:

    def __init__(self):
        self.secondsMap = {
\t\t\t\"day\": 86400,
\t\t\t\"hour\": 3600,
\t\t\t\"minute\": 60
\t\t}
        self.tweets = {}
        
    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName in self.tweets:
            self.tweets[tweetName].append(time)
        else:
            self.tweets[tweetName] = [time]

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        seconds = self.secondsMap[freq]
        bucket_size = int((endTime - startTime)/seconds)+1
        buckets = [0]*bucket_size
        if tweetName not in self.tweets:
            return []
        else:
            for t in self.tweets[tweetName]:
                if t >= startTime and t<= endTime:
                    bucket_index = int((t - startTime)/seconds)
                    buckets[bucket_index] += 1
        return buckets
                    
                
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
