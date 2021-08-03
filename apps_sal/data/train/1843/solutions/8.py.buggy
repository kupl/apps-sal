class TweetCounts:
    class TreeNode:
        def __init__(self,time,val=1,left=None,right=None):
            self.time = time
            self.val = val
            self.left = left
            self.right = right
            
    def __init__(self):
        self.tweets = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        def radd(root):
            if root.time == time:
                root.val += 1
            elif root.time > time:
                if root.left is None:
                    root.left = self.TreeNode(time)
                else:
                    radd(root.left)
            else:
                if root.right is None:
                    root.right = self.TreeNode(time)
                else:
                    radd(root.right)
        if tweetName not in self.tweets:
            self.tweets[tweetName] = self.TreeNode(time)
        else:
            radd(self.tweets[tweetName])

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        def rech(root,buckets,s):
            if root is not None:
                rech(root.left,buckets,s)
                if startTime <= root.time <= endTime:
                    while (startTime+len(buckets)*s)-1 < root.time: buckets.append(0)
                    buckets[-1] += root.val
                rech(root.right,buckets,s)
            return buckets
        s = 60 if freq == \"minute\" else 3600 if freq == \"hour\" else 86400
        buckets = rech(self.tweets[tweetName],[0],s)
        while (startTime+len(buckets)*s)-1 < endTime: buckets.append(0)
        return buckets
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
