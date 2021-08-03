class Solution:

    def find(self, u):
        if self.parent[u] == u:
            return u
        else:
            root_u = self.find(self.parent[u])
            self.parent[u] = root_u
            return self.find(self.parent[u])

    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        self.parent[parent_u] = parent_v

    def findCircleNum(self, M):
        if len(M) == 0:
            return 0
        n = len(M)
        self.parent = [i for i in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    self.union(i, j)
        friend_set = set()
        for i in range(n):
            friend_set.add(self.find(i))

        print(self.parent)
        return len(friend_set)
