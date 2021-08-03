class TweetCounts:

    def __init__(self):

        self.second = defaultdict(list)


    def recordTweet(self, tweetName: str, time: int) -> None:

        
        bisect.insort(self.second[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == \"minute\":
            step =  60
        elif freq == \"hour\":
            step = 3600
        else:
            step = 3600 * 24
            
        ans = []
        l = self.second[tweetName]
        while(startTime <= endTime):
            start, end = startTime, min(startTime + step-1, endTime)
            left, right = bisect.bisect_left(l, start), bisect.bisect_right(l, end)
            ans.append(right-left)
            startTime += step 
        return ans
        
    

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
