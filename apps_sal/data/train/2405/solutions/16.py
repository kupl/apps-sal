class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(tuple(t) for t in obstacles)
        
        turns = {}
        turns[('N', -1)] = 'E'
        turns[('E', -1)] = 'S'
        turns[('S', -1)] = 'W'
        turns[('W', -1)] = 'N'
        
        turns[('N', -2)] = 'W'
        turns[('W', -2)] = 'S'
        turns[('S', -2)] = 'E'
        turns[('E', -2)] = 'N'
        
        shifts = {}
        shifts['N'] = (0, 1)
        shifts['S'] = (0, -1)
        shifts['E'] = (1, 0)
        shifts['W'] = (-1,0)
        
        cur = [0,0]
        curD = 'N'
        
        res = 0
        for command in commands:
            if command < 0:
                curD = turns[(curD, command)]
            else:
                shift = shifts[curD]
                for i in range(command):
                    
                    tmp = [cur[0]+shift[0], cur[1]+shift[1]]
                    if tuple(tmp) in obs:
                        break
                    cur = tmp
                    res = max(res, cur[0]*cur[0] + cur[1]*cur[1])

        
            print(cur)
        return res
                    
                    
                    
        

