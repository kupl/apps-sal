class TweetCounts:

    def __init__(self):
        self.d = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.d:
            self.d[tweetName] = []
        arr = self.d[tweetName]
        i = len(arr)-1
        while i >= 0 and arr[i] > time:
            i -= 1
        self.d[tweetName] = arr[:i+1] + [time] + arr[i+1:]
        # assert self.d[tweetName] == sorted(self.d[tweetName])

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        # print(freq, tweetName, startTime, endTime, self.d)
        arr = self.d.get(tweetName, [])
        r = []
        j = 0
        step = (1 if freq == \"second\" else 
               60 if freq == \"minute\" else 
               60*60 if freq == \"hour\" else 
                60*60*24)
        while j < len(arr) and arr[j] < startTime:
            j += 1
        for i in range(startTime, endTime+1, step):
            r.append(0)
            while j < len(arr) and arr[j] <= min(i+step-1, endTime):
                j += 1
                r[-1] += 1
        return r


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
