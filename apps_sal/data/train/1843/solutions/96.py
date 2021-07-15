class TweetCounts:

    def __init__(self):
        self.db = {}
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.db:
            self.db[tweetName] = [time]

        elif tweetName in self.db:
            idx = len(self.db[tweetName])

            for i in range(len(self.db[tweetName])):
                if self.db[tweetName][i] >= time:
                    idx = i
                    break


            self.db[tweetName].insert(idx, time)

        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = 1

        if freq == \"minute\":
            # startTime *= 60
            # endTime *= 60
            delta *= 60

        elif freq == \"hour\":
            # startTime *= 60*60
            # endTime *= 60*60
            delta *= 60*60

        elif freq == \"day\":
            # startTime *= 60*60*12
            # endTime *= 60*60*12
            delta *= 60*60*12

        if tweetName not in self.db:
            # Would we instead want a list of zeroes.
            return [0]

        # delta -= 1
        
        start = startTime
        ans = []


        # Max val:
        maxTime = self.db[tweetName][-1]
        
        if startTime > maxTime:
    
            while start <= endTime:
                ans.append(0)

                start += delta
                
            return ans


        # Tweets
        tweets = self.db[tweetName]

        idx = 0

        while start > tweets[idx]:
            idx += 1

        # print(endTime)

        while start <= maxTime and start <= endTime:
            # print(start)
            tmp = 0

            while tweets[idx] <= endTime and start <= tweets[idx] < start+delta:

                tmp += 1

                if tweets[idx] == maxTime:
                    break

                idx += 1
                
            ans.append(tmp)
            start += delta
                
        while start <= endTime:
            ans.append(0)

            start += delta




        # Remove trailing zeroes

        return ans




# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
