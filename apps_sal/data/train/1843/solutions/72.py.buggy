class TweetCounts:

    def __init__(self):
        self.arr = collections.defaultdict(lambda: [])
        self.mapping = {\"hour\": 3600, \"minute\":60, \"day\":3600*24}

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.arr[tweetName], time)
            
        

    def getTweetCountsPerFrequency(self, freq: str, t: str, start: int, end: int) -> List[int]:
        ans = []
        interval = self.mapping[freq]
        while start<=end:
            ans.append(bisect.bisect_left(self.arr[t], min(end+1, start+interval)) - bisect.bisect_left(self.arr[t], start))
            start += interval
        return ans
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
