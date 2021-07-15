class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        i = 0
        pos = [0, 0]
        obstacles = set(tuple(x) for x in obstacles)
        max_dis = 0
        for num in commands:
            if num >= 0:
                for j in range(num):
                    pos[0] += direct[i][0]
                    pos[1] += direct[i][1]
                    if tuple(pos) in obstacles:
                        pos[0] -= direct[i][0]
                        pos[1] -= direct[i][1]
                        break
            else:
                if num == -1:
                    i = (i+1) % 4
                elif num == -2:
                    i = i-1 
                    if i < 0: i = 3
            
            max_dis = max(max_dis, pos[0]**2+pos[1]**2)
        return max_dis
