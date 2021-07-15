class User:
     
     def __init__(self,uid):
         self.uid=uid
         self.news =[]
         self.followee=set()
         
     def follow(self,followId):
         self.followee.add(followId)
     
     def unfollow(self,followId):
         if followId in self.followee:
             self.followee.remove(followId)
             
     def post(self,newsId):
         
         self.news.append(newsId)
         
 class Twitter:
 
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.user={}
         self.tweet={}
         self.tweetOrder=0
         
 
     def postTweet(self, userId, tweetId):
         """
         Compose a new tweet.
         :type userId: int
         :type tweetId: int
         :rtype: void
         """
         if userId not in self.user:
             self.user[userId]=User(userId)
         self.tweet[self.tweetOrder]=tweetId
         self.user[userId].post(self.tweetOrder)
         self.tweetOrder+=1
         
 
     def getNewsFeed(self, userId):
         """
         Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
         :type userId: int
         :rtype: List[int]
         """
         if userId not in self.user:
             return []
         newsFeed=[]
         relatedUser=[self.user[userId]]+[self.user[id] for id in self.user[userId].followee]
         for person in relatedUser:
             length=len(person.news)
             for i in range(min(10,length)):
                 if len(newsFeed)<10:
                     heapq.heappush(newsFeed,person.news[length-1-i])
                 else:
                     heapq.heappushpop(newsFeed,person.news[length-1-i])
         res=[]
         while newsFeed:
             res.append(heapq.heappop(newsFeed))
         return [self.tweet[tweetOrder] for tweetOrder in res[::-1]]
         
 
     def follow(self, followerId, followeeId):
         """
         Follower follows a followee. If the operation is invalid, it should be a no-op.
         :type followerId: int
         :type followeeId: int
         :rtype: void
         """
         if followerId != followeeId:
             if followerId not in self.user:
                 self.user[followerId]=User(followerId)
             if followeeId not in self.user:
                 self.user[followeeId]=User(followeeId)
             self.user[followerId].follow(followeeId)
         
 
     def unfollow(self, followerId, followeeId):
         """
         Follower unfollows a followee. If the operation is invalid, it should be a no-op.
         :type followerId: int
         :type followeeId: int
         :rtype: void
         """
         if followerId in self.user and followeeId in self.user:
             self.user[followerId].unfollow(followeeId)
         
 
 
 # Your Twitter object will be instantiated and called as such:
 # obj = Twitter()
 # obj.postTweet(userId,tweetId)
 # param_2 = obj.getNewsFeed(userId)
 # obj.follow(followerId,followeeId)
 # obj.unfollow(followerId,followeeId)
