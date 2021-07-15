class TweetCounts:

    def __init__(self):
        self.tweets = {} # {name:[n1,n2,n3]}
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweets.keys():
            self.tweets[tweetName] = []
        self.tweets[tweetName].append(time)
        # self.tweets[tweetName].sort()
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        
        if freq == \"hour\":
            gap = 60*60
        elif freq == \"day\":
            gap = 24*60*60
        else:
            gap = 60
            
        res = []
        if tweetName not in self.tweets.keys():
            return res
        
        tm = self.tweets[tweetName]
        
        for i in range(startTime, endTime+1, gap):
            sum=0
            end = min(i+gap, endTime+1)
            print(f\"i:{i} end:{end}\")
            
            for t in tm:
                if t >= i and t < end:
                    sum+=1
            res.append(sum)
            
        return res
        
        
            
        
                    
                    
                    


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
