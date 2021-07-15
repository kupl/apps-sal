class TweetCounts:

    def __init__(self):
        self.lst = []

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.lst.append((time, tweetName))

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        seconds=[24*3600, 3600, 60]
        F=[\"day\", \"hour\", \"minute\"]
        idx = F.index(freq)
        start = startTime
        end = endTime
        
        lens = (end-start+1+seconds[idx]-1)//seconds[idx]
        

        rs = [0]*lens
        for i, v in enumerate(self.lst):
            t = v[0]
            if t >= start and t <= end:
                if v[1] == tweetName:
                    #print(t, start, end, v[1])
                    rs[(t-start)//seconds[idx]] += 1
        return rs


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
