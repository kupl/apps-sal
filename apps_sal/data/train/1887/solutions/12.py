class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if M == None:
            return 0

        n = len(M)
        map1 = [[] for x in range(n)]

        # build graph
        for i in range(n):
            for j in range(n):
                if i != j and M[i][j] == 1:
                    if j not in map1[i]:
                        map1[i].append(j)
                    if i not in map1[j]:
                        map1[j].append(i)

        # bfs
        queue = collections.deque()
        hash1 = set()

        count = 0
        for i in range(n):
            if i not in hash1:
                count += 1
                queue.append(i)
                hash1.add(i)

                while queue:
                    node = queue.popleft()

                    for neighbor in map1[node]:
                        if neighbor in hash1:
                            continue
                        else:
                            queue.append(neighbor)
                            hash1.add(neighbor)
            queue.clear()

        return count
