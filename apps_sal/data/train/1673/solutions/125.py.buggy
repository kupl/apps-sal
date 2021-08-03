class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        above_others = [0] * len(arr[0]) #minimum path sum not including itself
        
        for row in arr:
            paths = [n + path for n, path in zip(row, above_others)]
            others = [float(\"inf\")] * len(paths)
            
            for r in range(len(paths)), reversed(range(len(paths))):
                min_path = float('inf')
                for i in r:
                    others[i] = min(others[i], min_path)
                    min_path = min(min_path, paths[i])
            
            above_others = others
        
        return min(above_others)
