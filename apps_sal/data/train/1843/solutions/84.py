class TweetNode:
    def __init__(self, time, count = 1):
        self.time       = time
        self._count     = count
        self.left_node  = None
        self.right_node = None
    
    def add_time(self, time):
        if self.time > time:
            if self.left_node is None:
                self.left_node = TweetNode(time)
            else:
                self.left_node.add_time(time)
        elif self.time < time:
            if self.right_node is None:
                self.right_node = TweetNode(time)
            else:
                self.right_node.add_time(time)
        else:
            self._count += 1
    
    def count(self, start_time, end_time):
        if self.time > end_time:
            return (self.left_node and self.left_node.count(start_time, end_time) or 0)
        elif self.time < start_time:
            return (self.right_node and self.right_node.count(start_time, end_time) or 0)
        else:
            return (
                self._count
                + (self.left_node  and self.left_node.count(start_time, end_time)  or 0)
                + (self.right_node and self.right_node.count(start_time, end_time) or 0)
            )
        
    def __str__(self):
        return '{ \"count\" : %s, \"time\" : %s, \"left\" : %s, \"right\" : %s }' % (self._count, self.time, str(self.left_node), str(self.right_node))
    
    def __repr__(self):
        return str(self)
            
class TweetCounts:

    def __init__(self):
        self.tweets = dict()

    def recordTweet(self, tweet_name: str, time: int) -> None:
        if tweet_name not in self.tweets:
            self.tweets[tweet_name] = TweetNode(time)
        else:
            self.tweets[tweet_name].add_time(time)

    def getTweetCountsPerFrequency(self, freq: str, tweet_name: str, start_time: int, end_time: int) -> List[int]:
        if tweet_name in self.tweets:
            if freq   == \"minute\":
                delta = 60
            elif freq == \"hour\":
                delta = 60 * 60
            elif freq == \"day\":
                delta = 60 * 60 * 24
            else:
                raise NotImplemented(\"The set frequency is not implemented.\")
            return [
                self.tweets[tweet_name].count(st, ((st + delta - 1) if (st + delta - 1) < end_time else end_time)) for st in range(start_time, end_time + 1, delta)
            ]
        else:
            return 0

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
