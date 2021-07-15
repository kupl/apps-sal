from sortedcontainers import SortedList

class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(SortedList)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].add(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        tweets = self.tweets[tweetName]
        if not tweets:
            return []
        
        bucket_size = {\"minute\": 60, \"hour\": 3600, \"day\": 3600*24}[freq]
        num_buckets = ceil((endTime-startTime)/bucket_size)
        if (endTime - startTime) % bucket_size == 0:
            num_buckets += 1
        buckets = [0] * num_buckets
        for t in tweets.irange(startTime, endTime):
            bucket_idx = floor((t - startTime) / bucket_size)
            buckets[bucket_idx] += 1
            
        return buckets
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
