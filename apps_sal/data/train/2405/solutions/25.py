class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obSet = set(map(tuple, obstacles))
        print(obSet)

        result = 0
        X = 0
        Y = 0
        directions = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        dirs = 0

        for i in commands:
            if i == -2:
                dirs = (dirs + 1) % 4
            elif i == -1:
                dirs = (dirs + 3) % 4

            else:
                for j in range(i):
                    new_X = X + directions[dirs][0]
                    new_Y = Y + directions[dirs][1]

                    if (new_X, new_Y) in obSet:
                        break

                    X = new_X
                    Y = new_Y
                result = max(result, X * X + Y * Y)
        return result
