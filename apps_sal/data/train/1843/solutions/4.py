class TweetCounts:
    def __init__(self):
        self.store = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.store[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = 0
        if freq == \"minute\":
            delta = 60
        elif freq == \"hour\":
            delta = 3600
        else:
            delta = 86400


        result=[0]* ((endTime-startTime)//delta +1)
        if not self.store[tweetName]:
            return result

        times=sorted(self.store[tweetName])
        for time in times:
            if startTime<=time<=endTime:
                result[(time-startTime)//delta]+=1

        return result

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
