class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adjList = {p: [] for p in range(1, N + 1)}
        for p1, p2 in dislikes:
            adjList[p1].append(p2)
            adjList[p2].append(p1)

        visited = set()
        for person in range(1, N + 1):
            if person not in visited:
                groups = [set([person]), set()]
                curList = [person]
                level = 0
                while curList:
                    next = []
                    curGroup = groups[level % 2]
                    theOtherGroup = groups[(level + 1) % 2]
                    for p in curList:
                        visited.add(p)
                        for neighbor in adjList[p]:
                            if neighbor in curGroup:
                                return False
                            if neighbor not in theOtherGroup:
                                theOtherGroup.add(neighbor)
                                next.append(neighbor)

                    curList = next
                    level += 1

        return True
