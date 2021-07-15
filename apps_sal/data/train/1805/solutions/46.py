class Solution:
    def createAdjMatrix(self,friends):
        adj_mat = {}
        for i in range(len(friends)):
            adj_mat[i] = friends[i]
        return adj_mat
    
    def calculateFreq(self,level_friend,watchedVideos):
        movies_freq = {}
        for friend in level_friend:
            movies = watchedVideos[friend]
            for movie in movies:
                movies_freq[movie] = movies_freq.get(movie,0)+1
                
        movies_freq = sorted(movies_freq.items(),key = lambda x:(x[1], x[0]))
        movies = [i[0] for i in movies_freq]
        return movies
    
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        
        adj_mat = self.createAdjMatrix(friends)
        visited = set()
        Q = [(id,0)]
        visited.add(id)
        level_friend = []
        while Q and level:
            id_,lev = Q.pop(0)
            if lev==level:
                level_friend.append(id_)
            if lev>level:
                break
            friends = adj_mat[id_]
            for friend in friends:
                if friend not in visited:
                    Q.append((friend,lev+1))
                    visited.add(friend)
                    
        return self.calculateFreq(level_friend,watchedVideos)
