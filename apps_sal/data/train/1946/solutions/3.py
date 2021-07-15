import heapq
 class Twitter:
 
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.users = {}
         self.twitters = {}
         self.time = 0
 
     def postTweet(self, userId, tweetId):
         """
         Compose a new tweet.
         :type userId: int
         :type tweetId: int
         :rtype: void
         """
         if userId in self.twitters:
             self.twitters[userId].append([-self.time, tweetId])
             self.time += 1
         else:
             self.twitters[userId] = [[-self.time, tweetId]]
             self.time+= 1
        
         if userId not in self.users:
             self.users[userId] = set([])
 
     def getNewsFeed(self, userId):
         """
         Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
         :type userId: int
         :rtype: List[int]
         """
         
         if userId not in self.users:
             return([])
             
         userIds = self.users[userId]
         
         if not userIds:
             userIds = set([])
         userIds.add(userId)
         newsArr = []
         for uId in userIds:
             if uId not in self.twitters:
                 newsArr.append([])
             else:
                 newsArr.append(self.twitters[uId][::-1])
         out = []
         heap = []
         for i in range(len(newsArr)):
             if newsArr[i]:
                 heapq.heappush(heap, [newsArr[i][0][0], newsArr[i][0][1], i, 0])
         while len(out) < 10:
             if len(heap) == 0:
                 break
             time,tId, arr, index = heapq.heappop(heap)
             out.append(tId)
             if index+1 < len(newsArr[arr]):
                 heapq.heappush(heap, [newsArr[arr][index+1][0],newsArr[arr][index+1][1],arr, index+1])
                 
         
         return([num for num in out])
         
 
     def follow(self, followerId, followeeId):
         """
         Follower follows a followee. If the operation is invalid, it should be a no-op.
         :type followerId: int
         :type followeeId: int
         :rtype: void
         """
    
         if followerId in self.users:
             self.users[followerId].add(followeeId)        
         else:
             self.users[followerId] = set([])
             self.users[followerId].add(followeeId) 
             
     def unfollow(self, followerId, followeeId):
         """
         Follower unfollows a followee. If the operation is invalid, it should be a no-op.
         :type followerId: int
         :type followeeId: int
         :rtype: void
         """
         if followerId in self.users:
             if followeeId in self.users[followerId]:
                 self.users[followerId].remove(followeeId)
 
 # Your Twitter object will be instantiated and called as such:
 # obj = Twitter()
 # obj.postTweet(userId,tweetId)
 # param_2 = obj.getNewsFeed(userId)
 # obj.follow(followerId,followeeId)
 # obj.unfollow(followerId,followeeId)
