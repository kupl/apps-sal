from sortedcontainers import SortedList

class TweetCounts:
    freq_seconds = {
        'minute': 60,
        'hour': 3600,
        'day': 86400,
    }
    
    def __init__(self):
        self.tweets: Dict[str, List[int]] = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweets:
            self.tweets[tweetName] = SortedList()
        self.tweets[tweetName].add(time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        interval = self.freq_seconds[freq]
        counts = []
        times = self.tweets.get(tweetName, [])
        bucket_start = startTime
        index_start = times.bisect_left(bucket_start)
        while bucket_start <= endTime:
            bucket_end = min(bucket_start + interval, endTime + 1)
            index_end = times.bisect_left(bucket_end)
            counts.append(index_end - index_start)
            bucket_start = bucket_end
            index_start = index_end
        return counts


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

