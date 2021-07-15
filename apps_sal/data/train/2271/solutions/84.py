class Union_Find():
    def __init__(self,N):
        """0,1,...,n-1を要素として初期化する.

        n:要素数
        """
        self.n=N
        self.parents=[-1]*N
        self.rank=[0]*N

    def find(self, x):
        """要素xの属している族を調べる.

        x:要素
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """要素x,yを同一視する.

        x,y:要素
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x]>self.rank[y]:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
        else:
            self.parents[y] += self.parents[x]
            self.parents[x] = y

            if self.rank[x]==self.rank[y]:
                self.rank[y]+=1

    def size(self, x):
        """要素xの属している要素の数.

        x:要素
        """
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """要素x,yは同一視されているか?

        x,y:要素
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """要素xが属している族の要素.
        ※族の要素の個数が欲しいときはsizeを使うこと!!

        x:要素
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """族の名前のリスト
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """族の個数
        """
        return len(self.roots())

    def all_group_members(self):
        """全ての族の出力
        """
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
#================================================
N,M=map(int,input().split())
P=list(map(lambda x:int(x)-1,input().split()))

U=Union_Find(N)
for _ in range(M):
    a,b=map(int,input().split())
    U.union(a-1,b-1)

K=0
for x in range(N):
    K+=U.same(x,P[x])
print(K)
