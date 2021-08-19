# 이웃수가 가장 적은 노드 찾기
# 이웃수가 같다면 번호가 가장 큰 노드 반환

# 1. 모든 노드 다익스트라
# 2. 플로이드와샬
# 우선 adj 만들기
# adj에 연결되 있는 부분 값 넣어주기

# if adj[i][j] + adj[j][k] < adj[i][k]
# adj[i][k] = adj[i][j] + adj[j][k]
def floydWarshall(adj, n):
    #     처음에 출발지, 도착지, 경유지 순서로 했을 때는 틀림 왜일까?
    for k in range(n):  # 경유지
        for i in range(n):  # 출발지
            for j in range(n):  # 도착지
                stopOver = adj[i][k] + adj[k][j]
                if(stopOver < adj[i][j]):
                    adj[i][j] = stopOver


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INFI = 2 ** 31
        adj = [[INFI for _ in range(n)] for _ in range(n)]
        answer = 0
        neighbors = []
        for x in range(n):
            adj[x][x] = 0

        for edge in edges:
            adj[edge[0]][edge[1]] = edge[2]
            adj[edge[1]][edge[0]] = edge[2]
        floydWarshall(adj, n)
        # print(adj)
#         이웃 추가
        for node in adj:
            count = 0  # 이웃 수
            for distance in node:
                if distance <= distanceThreshold:
                    count += 1
            neighbors.append(count - 1)

        # print(neighbors)
        minCount = min(neighbors)
        # print(neighbors)
        for i, neighCount in enumerate(neighbors):
            if(minCount == neighCount):
                answer = i

        return answer
