class Solution:
    def backtracking(self,result,visited,n,found):
        if len(result) == 2 ** n:
            diff = abs(result[-1] - result[0])
            while diff%2 == 0:
                diff = diff/2
            if diff == 1:
                found[0] = 1
            return
        if found[0] == 1:
            return
        start = result[-1]
        for i in range(n):
            num = start ^ (1 << i)
            if num in visited or num<0 or num>=2 ** n:
                continue
            result.append(num)
            visited[num] = 1
            self.backtracking(result,visited,n,found)
            if found[0] == 1:
                return
            visited.pop(num)
            result.pop()
        
    def circularPermutation(self, n: int, start: int) -> List[int]:
        if n == 0:
            return [0]
        result = [start]
        found = [0]
        visited = {}
        visited[start] = 1
        self.backtracking(result,visited,n,found)
        return result
