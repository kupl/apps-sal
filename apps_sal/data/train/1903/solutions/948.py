class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        c = collections.defaultdict(list)
        for i in range(l - 1):
            for j in range(i + 1, l):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                c[d].append((i, j))
        tocons = list(sorted(c.keys()))
        # print(tocons)

        def isCyclicUtil(v, visited, parent, graph):
            visited[v] = True
            for i in graph[v]:
                if visited[i] == False:
                    if isCyclicUtil(i, visited, v, graph):
                        return True
                elif parent != i:
                    return True
            return False

        def checkloop(y, connected, edges):
            if y[0] not in connected or y[1] not in connected:
                return True
            root = y[0]

            visited = [False] * (l)

            graph = collections.defaultdict(list)
            graph[y[0]] = [y[1]]
            graph[y[1]] = [y[0]]
            for x in edges:
                graph[x[0]].append(x[1])
                graph[x[1]].append(x[0])
            for i, x in enumerate(connected):
                if visited[x] == False:
                    if isCyclicUtil(x, visited, -1, graph) == True:
                        return False
            '''
            seq=[root]
            seen=set()
            seen.add(root)
            while seq:
                v=seq.pop()
                for w in graph[v]:
                    if w not in seen:
                        if isCyclicUtil(w,visited,v,graph):
                            return False
                        seq.append(w)
            '''
            return True

        edges = []
        count = 0
        cost = 0
        connected = set()
        for x in tocons:
            for y in c[x]:
                # print(y,x,connected,count)

                if checkloop(y, connected, edges):
                    count += 1
                    cost += x
                    connected.add(y[0])
                    connected.add(y[1])
                    edges.append(y)
                if count == l - 1:
                    return cost
        return 0
