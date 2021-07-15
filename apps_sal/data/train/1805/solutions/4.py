class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        bfs,visited={id},{id}
        for _ in range(level):
            bfs={j for i in bfs for j in friends[i] if j not in visited}
            visited|=bfs
        freq=collections.Counter([v for idx in bfs for v in watchedVideos[idx]])
        return sorted(list(freq.keys()),key=lambda x:(freq[x],x))
#         d = defaultdict(list)
#         for i in range(len(friends)):
#             d[i].extend(friends[i])
        
#         videoCounts = []
#         for i in range(len(watchedVideos)):
#             videoCounts.append(len(watchedVideos[i]))
        
#         output = defaultdict(int)
#         q = []
#         q.append((id, 0))
#         while q:
#             node, lev = q.pop(0)
#             if lev > level:
#                 continue
#             if lev == level:
#                 for movie in watchedVideos[node]:
#                     output[movie] += 1
#                 continue
#             else:
#                 for nei in d[node]:
#                     q.append((nei, lev + 1))
        
#         ans = []
#         for key in output:
#             ans.append((key, output[key]))
#         ans.sort(key=lambda x: x[1])
#         return list(map(lambda x: x[0], ans))

