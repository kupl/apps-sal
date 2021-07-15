import queue
 import heapq
     
 class Twitter:
     def _addUser(self, userId):
         if userId not in self.tweets:
             self.tweets[userId] = []
         if userId not in self.graph:
             self.graph[userId] = set([userId])
 
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.graph = {}
         self.tweets = {}
         self.now = 0
         
 
     def postTweet(self, userId, tweetId):
         """
         Compose a new tweet.
         :type userId: int
         :type tweetId: int
         :rtype: void
         """
         self.now -= 1
         self._addUser(userId)
         self.tweets[userId].append((self.now, tweetId))
         self.follow(userId, userId)
         
 
     def getNewsFeed(self, userId):
         """
         Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
         :type userId: int
         :rtype: List[int]
         """
         self._addUser(userId)
         h = []
         for followee in self.graph[userId]:
             numtweets = len(self.tweets[followee])
             if numtweets > 10:
                 for tweet in self.tweets[followee][numtweets - 10:]:
                     h.append(tweet)
             else:
                 for tweet in self.tweets[followee]:
                     h.append(tweet)
         heapq.heapify(h)
         lst = []
         while len(h) > 0 and len(lst) < 10:
             elem = heapq.heappop(h)
             lst.append(elem[1])
         return lst
                 
 
     def follow(self, followerId, followeeId):
         """
         Follower follows a followee. If the operation is invalid, it should be a no-op.
         :type followerId: int
         :type followeeId: int
         :rtype: void
         """
         self._addUser(followerId)
         self._addUser(followeeId)
         self.graph[followerId].add(followeeId)
         
 
     def unfollow(self, followerId, followeeId):
         """
         Follower unfollows a followee. If the operation is invalid, it should be a no-op.
         :type followerId: int
         :type followeeId: int
         :rtype: void
         """
         self._addUser(followerId)
         if followeeId != followerId:
             self.graph[followerId].discard(followeeId)
 
 
 # Your Twitter object will be instantiated and called as such:
 # obj = Twitter()
 # obj.postTweet(userId,tweetId)
 # param_2 = obj.getNewsFeed(userId)
 # obj.follow(followerId,followeeId)
 # obj.unfollow(followerId,followeeId)
