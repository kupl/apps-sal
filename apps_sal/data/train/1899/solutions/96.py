class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        found_y, found_x = None, None
        for y in range(len(A)):
            found_one = False
            for x in range(len(A[0])):
                if A[y][x] == 1:
                    found_y, found_x = y, x
                    A = self.invertOnes(y, x, A)
                    found_one = True
                    break
            if found_one:
                break

        return self.BFS(found_y, found_x, A)

    def invertOnes(self, y, x, A):
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        stack = []
        stack.append((y, x))
        A[y][x] = -1

        while stack:
            curr_y, curr_x = stack.pop(0)

            for neighbor in neighbors:
                new_y, new_x = curr_y + neighbor[0], curr_x + neighbor[1]
                if new_y >= 0 and new_y < len(A) and new_x >= 0 and new_x < len(A[0]) and A[new_y][new_x] == 1:
                    A[new_y][new_x] = -1
                    stack.append((new_y, new_x))

        return A

    def BFS(self, y, x, A):
        visited = {}
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        stack = []
        stack.append((y, x, 0))
        visited[(y, x)] = 0
        min_dist = float('inf')

        while stack:
            curr_y, curr_x, curr_dist = stack.pop(0)
            if A[curr_y][curr_x] == 1:
                min_dist = min(min_dist, curr_dist - 1)

            for neighbor in neighbors:
                new_y, new_x = curr_y + neighbor[0], curr_x + neighbor[1]
                if new_y >= 0 and new_y < len(A) and new_x >= 0 and new_x < len(A[0]):
                    if A[new_y][new_x] == -1:
                        new_dist = 0
                    else:
                        new_dist = curr_dist + 1

                    if (new_y, new_x) not in visited:
                        stack.append((new_y, new_x, new_dist))
                        visited[(new_y), (new_x)] = new_dist
                    else:
                        if visited[(new_y), (new_x)] > new_dist:
                            visited[(new_y), (new_x)] = new_dist
                            stack.append((new_y, new_x, new_dist))

        return min_dist
