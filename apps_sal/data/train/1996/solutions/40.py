class Solution:
    data = {}

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result = []
        # print(result, self.data)
        self.data = {}
        for i in range(len(graph)):
            if i in self.data:
                if self.data[i]:
                    result.append(i)
            else:
                res = self.check(graph, i, [])
                if res == True:
                    result.append(i)
                    self.data[i] = True

        return result

    def check(self, graph, curr, path):
        if curr in path:
            self.data[curr] = False
            for p in path:
                self.data[p] = False
            return False

        if len(graph[curr]) == 0:
            self.data[curr] = True
            return True

        result = True
        for n in graph[curr]:
            if n == curr:
                self.data[n] = False
                return False

            if n in self.data:
                result = result and self.data[n]
            else:
                res = self.check(graph, n, path + [curr])
                result = result and res
            if result == False:
                return False

        if result == True:
            self.data[curr] = True

        return True
