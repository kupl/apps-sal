class Solution:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = (0, 1)

        self.obstacleSet = set()

    def _turnLeft(self):
        newXDirection = -self.direction[1]
        newYDirection = self.direction[0]
        self.direction = (newXDirection, newYDirection)

    def _turnRight(self):
        newXDirection = self.direction[1]
        newYDirection = -self.direction[0]
        self.direction = (newXDirection, newYDirection)

    def _tryMoveForward(self, numUnits):
        canMoveNumUnits = 0

        xMove = self.direction[0]
        yMove = self.direction[1]

        for i in range(1, numUnits + 1):
            newX = self.x + (xMove * i)
            newY = self.y + (yMove * i)

            if (newX, newY) not in self.obstacleSet:
                canMoveNumUnits = i
            else:
                break
        return canMoveNumUnits

    def _move(self, numUnits):
        self.x += self.direction[0] * numUnits
        self.y += self.direction[1] * numUnits

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        maxDistance = 0

        for obstacle in obstacles:
            self.obstacleSet.add(tuple(obstacle))

        for command in commands:
            if command == -2:
                self._turnLeft()
            elif command == -1:
                self._turnRight()
            else:
                canMoveNumUnits = self._tryMoveForward(command)
                self._move(canMoveNumUnits)

                maxDistance = max(maxDistance, self.x ** 2 + self.y ** 2)

        return maxDistance
