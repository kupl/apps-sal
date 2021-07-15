class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        '''
        Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
        visited = {(1,1), (1,3)}
        '''
        visited = set()
        output = float('inf')
        for x1, y1 in points:
            for x2, y2 in visited:
                if (x1, y2) in visited and (x2, y1) in visited:
                    temp = abs(x2 - x1) * abs(y2 - y1)
                    if temp < output:
                        output = temp
            visited.add((x1, y1))
        return output if output != float('inf') else 0
