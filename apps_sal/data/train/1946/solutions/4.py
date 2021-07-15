from heapq import heappush, heappop
 
 class Twitter:
     time_stamp = 0
     class User:
         def __init__(self, user_id):
             self.user_id = user_id
             self.followers = set()
             self.follow(user_id)
             self.tweet_head = None
             
         def follow(self, follower_id):
             self.followers.add(follower_id)
         
         def unfollow(self, follower_id):
             if follower_id in self.followers:
                 self.followers.remove(follower_id)
                 
         def post(self, new_tweet):
             nxt = self.tweet_head
             self.tweet_head, new_tweet.next = new_tweet, nxt
     
     class Tweet:
         def __init__(self, tw_id, ts):
             self.tweet_id = tw_id
             self.timestamp = ts
             self.next = None            
     
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.user_map = {}
         
 
     def postTweet(self, userId, tweetId):
         """
         Compose a new tweet.
         :type userId: int
         :type tweetId: int
         :rtype: void
         """
         if userId not in self.user_map:
             self.user_map[userId] = self.User(userId)
         user = self.user_map[userId]
         user.post(self.Tweet(tweetId, self.time_stamp))
         self.time_stamp += 1
 
     def getNewsFeed(self, userId):
         """
         Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
         :type userId: int
         :rtype: List[int]
         """
         ans, pq = [], []
         if userId not in self.user_map:
             return ans
         user = self.user_map[userId]
         for follower in user.followers:
             tw = self.user_map[follower].tweet_head
             if tw:
                 heappush(pq, (-tw.timestamp, tw))
         n = 10
         while pq and n > 0:
             ts, tw = heappop(pq)
             ans.append(tw.tweet_id)
             nxt = tw.next
             if nxt:                
                 heappush(pq, (-nxt.timestamp, nxt))
             n -= 1
         return ans
             
 
     def follow(self, followerId, followeeId):
         """
         Follower follows a followee. If the operation is invalid, it should be a no-op.
         :type followerId: int
         :type followeeId: int
         :rtype: void
         """
         if followerId not in self.user_map:
             self.user_map[followerId] = self.User(followerId)            
         if followeeId not in self.user_map:
             self.user_map[followeeId] = self.User(followeeId)
         self.user_map[followerId].follow(followeeId)
 
     def unfollow(self, followerId, followeeId):
         """
         Follower unfollows a followee. If the operation is invalid, it should be a no-op.
         :type followerId: int
         :type followeeId: int
         :rtype: void
         """
         if followerId not in self.user_map or followeeId not in self.user_map or followerId == followeeId:
             return
         self.user_map[followerId].unfollow(followeeId)
 
         
 
 
 # Your Twitter object will be instantiated and called as such:
 # obj = Twitter()
 # obj.postTweet(userId,tweetId)
 # param_2 = obj.getNewsFeed(userId)
 # obj.follow(followerId,followeeId)
 # obj.unfollow(followerId,followeeId)
