class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        maxD2 = 0
        pos = [0, 0]
        ori = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        pOri = 0
        obsSet = set()
        for i in obstacles:
            obsSet.add(tuple(i))
        for i in commands:
            if i == -1:
                pOri += 1
                pOri %= 4
            elif i == -2:
                pOri -= 1
                pOri %= 4
            else:
                n = 1
                while n <= i:
                    tempx = pos[0] + ori[pOri][0]
                    tempy = pos[1] + ori[pOri][1]
                    if (tempx, tempy) not in obsSet:
                        pos[0] = tempx
                        pos[1] = tempy
                        n += 1
                    else:
                        break
                maxD2 = max(maxD2, pos[0] ** 2 + pos[1] ** 2)
        return maxD2
