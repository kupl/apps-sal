class TweetCounts:

    def __init__(self):
        self.data = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.data[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        T, d = self.data[tweetName], 60 if freq == \"minute\" else (3600 if freq == \"hour\" else 86400)
        ans = [0]*((endTime-startTime)//d + 1)
        for i in range(bisect.bisect_left(T, startTime), bisect.bisect(T, endTime)):
            ans[(T[i]-startTime)//d] += 1
        return ans
    

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
