class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        stack = [(0, id)]
        visited = set([id])
        friendsSet = set()
        while stack:
            lNow, fi = heapq.heappop(stack)
            if lNow == level:
                friendsSet.add(fi)
            else:
                for fi1 in friends[fi]:
                    if fi1 not in visited:
                        visited.add(fi1)
                        heapq.heappush(stack, (lNow+1, fi1))
        videoCounter = Counter()
        for f in friendsSet:
            videoCounter += Counter(watchedVideos[f])
            
        ans = sorted([key for key in videoCounter], key = lambda x: (videoCounter[x],x) )
        # print(videoCounter)
        return ans        
#         friendsSet = set()
#         visited = set()
#         visited.add(id)
#         def findFriends(fi0, l0):
#             if l0 == level:
#                 if fi0 not in visited:
#                     visited.add(fi0)
#                     friendsSet.add(fi0)
#                 return
#             visited.add(fi0)
#             for fi1 in friends[fi0]:
#                 if fi1 not in visited:
#                     findFriends(fi1, l0 + 1)
        
#         findFriends(id, 0)
#         videoCounter = Counter()
#         for f in friendsSet:
#             videoCounter += Counter(watchedVideos[f])
            
#         ans = sorted([key for key in videoCounter], key = lambda x: (videoCounter[x],x) )
#         # print(videoCounter)
#         return ans

