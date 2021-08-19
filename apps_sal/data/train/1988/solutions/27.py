class Solution:
    # TLE
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        '''
        O(N^3)

        Variation of Floyd.

        DP.

        dp[k, i, j, c1, c2]:
        shortest path between i and j, 
        with first edge being c1 and last edge being color c2, 
        using first k nodes as intermediary.

        Transition: 
        - for each k, try if it it is an improvement for (i, j, c1, c2)
        - 1) 
          - dp[k - 1, i, k, c1, 0] + dp[k - 1, k, j, 1, c2] -- use k to improve
          - dp[k - 1, i, k, c1, 1] + dp[k - 1, k, j, 0, c2] -- use k to improve
        - 2) dp[k - 1, i, j, c1, c2] -- do not use k (but used up to k-1) 

        Since k is executed in increasing order, we can remove this dimension by rollling array.

        Use dict(<i, j, c1, c2>) to store the state.

        '''

        MAX = float('inf')

        state = {}
        for i in range(n):
            for j in range(n):
                for c1 in range(2):
                    for c2 in range(2):
                        state[(i, j, c1, c2)] = MAX

        for u, v in red_edges:
            state[(u, v, 0, 0)] = 1
            # state[(v, u, 0, 0)] = 1
        for u, v in blue_edges:
            state[(u, v, 1, 1)] = 1
            # state[(v, u, 1, 1)] = 1

        def relax(k):
            for i in range(n):
                for j in range(n):
                    for c1 in range(2):
                        for c2 in range(2):
                            state[(i, j, c1, c2)] = min(
                                state[(i, j, c1, c2)],
                                state[(i, k, c1, 0)] + state[(k, j, 1, c2)],
                                state[(i, k, c1, 1)] + state[(k, j, 0, c2)]
                            )

        for k in range(0, n):
            # if k == 5:
            #     print(state[(5, 5, 0, 0)])
            #     print(state[(5, 5, 1, 1)])
            #     print(state[(0, 5, 1, 0)])
            #     print(state[(0, 5, 1, 1)])
            #     print(state[(5, 2, 0, 0)])
            #     print(state[(5, 2, 1, 0)])
            relax(k)

        # print('end', state[(5, 2, 1, 0)])

        for k in range(0, n):
            relax(k)

        # print('end', state[(5, 2, 1, 0)])

        ans = [0]
        for i in range(1, n):
            t = min(state[(0, i, c1, c2)] for c1 in range(2) for c2 in range(2))
            if t == MAX:
                t = -1
            ans.append(t)

        return ans


'''
3
[[0,1],[1,2]]
[]
3
[[0,1]]
[[2,1]]
3
[[1,0]]
[[2,1]]
3
[[0,1]]
[[1,2]]
3
[[0,1],[0,2]]
[[1,0]]
5
[[0,1],[1,2],[0,3],[4,2]]
[[3,4]]
6
[[4,1],[3,5],[5,2],[1,4],[4,2],[0,0],[2,0],[1,1]]
[[5,5],[5,0],[4,4],[0,3],[1,0]]
100
[[42,98],[85,41],[71,93],[2,38],[51,81],[0,17],[62,95],[76,15],[96,12],[98,38],[22,22],[26,65],[32,81],[23,33],[95,3],[18,8],[14,49],[60,23],[47,18],[38,82],[22,53],[6,79],[54,81],[37,44],[20,75],[22,33],[70,20],[94,24],[75,44],[19,78],[17,58],[11,47],[18,30],[17,65],[43,1],[18,5],[0,68],[82,75],[66,12],[41,67],[41,86],[37,48],[86,89],[41,1],[28,68],[19,47],[97,60],[59,3],[0,19],[77,91],[77,34]]
[[61,11],[34,19],[18,61],[45,60],[80,28],[33,6],[51,45],[54,56],[42,12],[8,4],[74,64],[57,66],[98,25],[40,84],[2,34],[80,41],[35,47],[5,19],[87,32],[6,3],[64,94],[60,67],[75,95],[72,6],[89,0],[44,63],[27,62],[56,54],[26,9],[46,66],[79,40],[83,14],[44,73],[93,77],[14,48],[65,20],[57,30],[99,46],[85,80],[25,24],[99,4],[6,45],[25,51],[47,44]]
'''


class Solution:
    # AC
    # Runtime: 144 ms, faster than 22.01% of Python3 online submissions for Shortest Path with Alternating Colors.
    # Memory Usage: 14.2 MB, less than 10.36% of Python3 online submissions for Shortest Path with Alternating Colors.
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        '''
        modified SPFA (Dijkstra)

        PriorityQueue element: (node, end_edge_color).
        O(M log M)
        '''

        MAX = float('inf')

        from collections import defaultdict
        adj = defaultdict(set)
        for u, v in red_edges:
            adj[u].add((v, 0))
        for u, v in blue_edges:
            adj[u].add((v, 1))

        from queue import PriorityQueue
        pq = PriorityQueue()
        pq.put((0, 0, 0))  # distance, node, color
        pq.put((0, 0, 1))
        dist = {}
        for u in range(n):
            for c in range(2):
                dist[(u, c)] = MAX
        dist[(0, 0)] = 0
        dist[(0, 1)] = 0
        # solved = {}
        solved = set()
        while not pq.empty():
            d, u, c = pq.get()
            # solved[(u, c)] = d
            for v, cc in adj[u]:
                if cc != c:
                    if dist[(v, cc)] > d + 1:
                        dist[(v, cc)] = d + 1
                        pq.put((d + 1, v, cc))

        ans = []
        for u in range(n):
            t = min(dist[(u, 0)], dist[(u, 1)])
            if t == MAX:
                t = -1
            ans.append(t)

        return ans


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        '''
        Idea: We can switch edge and node.

        In the new graph definition:
        - node: original edges, regardless of their color
        - edge: 
            we test all pairs of original incident edges (now node) at one original node, 
            build an edge if they are of different color

        Run normal SP algorithm on the resulting graph.
        '''

        from collections import defaultdict
        ri, ro, bi, bo = defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)

        nodes = set()
        for (i, (u, v)) in enumerate(red_edges):
            nodes.add(('r', i))
            ro[u].append(('r', i))
            ri[v].append(('r', i))
        for (i, (u, v)) in enumerate(blue_edges):
            nodes.add(('b', i))
            bo[u].append(('b', i))
            bi[v].append(('b', i))

        graph = defaultdict(set)
        for i in range(n):
            for u in ri[i]:
                for v in bo[i]:
                    graph[u].add(v)
            for u in bi[i]:
                for v in ro[i]:
                    graph[u].add(v)

        nodes.add('S')
        for u in ro[0]:
            graph['S'].add(u)
        for u in bo[0]:
            graph['S'].add(u)

        INF = float('inf')
        dist = {}
        for u in nodes:
            dist[u] = INF
        dist['S'] = 0

        from queue import PriorityQueue
        pq = PriorityQueue()
        pq.put((0, 'S'))
        solved = set()
        while len(solved) < len(nodes) and not pq.empty():
            d, u = pq.get()
            solved.add(u)
            for v in graph[u]:
                if dist[u] + 1 < dist[v]:
                    dist[v] = d + 1
                    pq.put((d + 1, v))

        ans = [0]
        for i in range(1, n):
            rd = [dist[u] for u in ri[i]]
            bd = [dist[u] for u in bi[i]]
            if len(rd + bd) == 0:
                t = -1
            else:
                t = min(rd + bd)
                if t == INF:
                    t = -1
            ans.append(t)

        return ans
