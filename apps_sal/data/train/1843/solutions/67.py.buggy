class TweetCounts:

    def __init__(self):
        self.d={}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if(tweetName in self.d):
            self.d[tweetName].append(time)
        else:
            self.d[tweetName]=[time]
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if(tweetName not in self.d):
            return [0]
        a=self.d[tweetName]
        if(freq==\"minute\"):
            c=[0 for i in range(1+((endTime-startTime)//60))]
            for i in a:
                if(i>=startTime)and(i<=endTime):
                    c[(i-startTime)//60]+=1
            return c
        if(freq==\"hour\"):
            c=[0 for i in range(1+((endTime-startTime)//3600))]
            for i in a:
                if(i>=startTime)and(i<=endTime):
                    c[(i-startTime)//3600]+=1
            return c
        if(freq==\"day\"):
            c=[0 for i in range(1+((endTime-startTime)//86400))]
            for i in a:
                if(i>=startTime)and(i<=endTime):
                    c[(i-startTime)//86400]+=1
            return c
            


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
