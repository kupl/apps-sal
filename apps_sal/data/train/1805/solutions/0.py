class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        vis = [0 for i in range(len(friends))]
        index = id
        lis = set([id])
        while level>0:
            temp = []
            for i in lis:
                if vis[i] == 0:
                    #print(i)
                    temp += friends[i]
                    vis[i] = 1
            lis = set(temp)
            level -= 1
        dic = dict()
        for i in lis:
            if vis[i] == 0:
                for j in watchedVideos[i]:
                    if j in dic:
                        dic[j]+=1
                    else:
                        dic[j] = 1
        dic2 = dict()
        for i in dic:
            if dic[i] in dic2:
                dic2[dic[i]].append(i)
            else:
                dic2[dic[i]] = [i]
        lis = []
        for i in sorted(dic2.keys()):
            lis += sorted(dic2[i])
        return lis

