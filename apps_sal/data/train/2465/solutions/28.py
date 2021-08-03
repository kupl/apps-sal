class Solution:
    def divisorGame(self, N: int) -> bool:

        self.visited = collections.defaultdict(bool)

        def alice_wins(N, alice=True):

            if N == 1:
                return True if not alice else False

            if N in self.visited:
                return self.visited[N]

            for i in range(1, N):
                if not N % i:
                    if alice:
                        self.visited[N] = alice_wins(N - i, alice=False)
                    else:
                        self.visited[N] = alice_wins(N - i)

            return self.visited[N]

        return alice_wins(N)
