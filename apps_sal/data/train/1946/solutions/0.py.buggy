from collections import defaultdict, deque
 from heapq import merge
 from itertools import islice
 
 class Twitter:
 
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.id2tweets = defaultdict(deque)
         self.id2follows = defaultdict(set)
         self.uid = 0
 
     def postTweet(self, userId, tweetId):
         """
         Compose a new tweet.
         :type userId: int
         :type tweetId: int
         :rtype: void
         """
         self.id2tweets[userId].appendleft((self.uid, tweetId))
         self.uid -= 1
         #print(userId, 'POST', tweetId, self.id2tweets)
 
     def getNewsFeed(self, userId):
         """
         Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
         :type userId: int
         :rtype: List[int]
         """
         #print('GET', userId, self.id2tweets, self.id2follows)
         tweets = heapq.merge(*(self.id2tweets[u] for u in self.id2follows[userId] | {userId}))
         return [tweet_id for _, tweet_id in islice(tweets, 10)]
 
     def follow(self, followerId, followeeId):
         """
         Follower follows a followee. If the operation is invalid, it should be a no-op.
         :type followerId: int
         :type followeeId: int
         :rtype: void
         """
         self.id2follows[followerId].add(followeeId)
         #print(followerId, 'FOLLOW', followeeId, self.id2follows)
 
     def unfollow(self, followerId, followeeId):
         """
         Follower unfollows a followee. If the operation is invalid, it should be a no-op.
         :type followerId: int
         :type followeeId: int
         :rtype: void
         """
         self.id2follows[followerId].discard(followeeId)
         #print(followerId, 'UNFOLLOW', followeeId, self.id2follows)
 
 # Your Twitter object will be instantiated and called as such:
 # obj = Twitter()
 # obj.postTweet(userId,tweetId)
 # param_2 = obj.getNewsFeed(userId)
 # obj.follow(followerId,followeeId)
 # obj.unfollow(followerId,followeeId)
