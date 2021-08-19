class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        edgesDict = defaultdict(list)

        for edgeType, src, dst in edges:
            edgesDict[src].append((edgeType, dst))
            edgesDict[dst].append((edgeType, src))

        visited = set()

        clusters = []
        cur_cluster = []

        def DFS(cur):
            visited.add(cur)
            cur_cluster.append(cur)
            for edge in edgesDict[cur]:
                if edge[0] == 3:
                    neighbor = edge[1]
                    if neighbor not in visited:
                        DFS(neighbor)

        for i in range(1, n + 1):
            if i not in visited:
                cur_cluster = []
                DFS(i)
                clusters.append(cur_cluster)

        #print('clusters', clusters)

        nodeToClusterDict = dict()
        for idx, cur_cluster in enumerate(clusters):
            for node in cur_cluster:
                nodeToClusterDict[node] = idx

        #print('nodeToClusterDict', nodeToClusterDict)
        clusterEdges = defaultdict(set)

        def doit(this_type):
            clusterEdges = defaultdict(set)
            for edgeType, src, dst in edges:
                if edgeType == this_type and nodeToClusterDict[src] != nodeToClusterDict[dst]:
                    src_cluster, dst_cluster = nodeToClusterDict[src], nodeToClusterDict[dst]
                    clusterEdges[src_cluster].add(dst_cluster)
                    clusterEdges[dst_cluster].add(src_cluster)

            #print('this_type', this_type, 'clusterEdges', clusterEdges)
            visitedClusters = set()

            def DFSCluster(cur_cluster):
                #print('visit cluster', cur_cluster)
                visitedClusters.add(cur_cluster)

                for neighbor_cluster in clusterEdges[cur_cluster]:
                    if neighbor_cluster not in visitedClusters:
                        DFSCluster(neighbor_cluster)

            DFSCluster(0)
            if len(visitedClusters) == len(clusters):
                # all clusters can be visited
                return len(clusters) - 1
            else:
                return -1

        ans1, ans2 = doit(1), doit(2)

        if ans1 >= 0 and ans2 >= 0:
            return len(edges) - (ans1 + ans2 + sum(len(x) - 1 for x in clusters))
        else:
            return -1
