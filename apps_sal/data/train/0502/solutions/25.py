class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        d = collections.defaultdict(list)
        initial.sort()

        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if i != j and graph[i][j] == 1:
                    d[i].append(j)
                else:
                    d[i].append(100)
                    d[i].pop()
        print(d)

        infected = set(initial)

        maxinfected = float('inf')
        res = 0
        for i in range(len(initial)):
            self.curr_infected = 0
            infected.remove(initial[i])

            visited = set()
            for item in infected:
                self.dfs(item, d, visited, infected, True)

            print((self.curr_infected))
            if self.curr_infected < maxinfected:
                maxinfected = self.curr_infected
                res = initial[i]

            infected.add(initial[i])

        return res

    def dfs(self, curr, d, visited, infected, original_node):
        if curr in visited:
            return
        if curr in infected and not original_node:
            return
        original_node = False

        visited.add(curr)
        self.curr_infected += 1

        neighbors = d[curr]

        for next in neighbors:
            self.dfs(next, d, visited, infected, original_node)
