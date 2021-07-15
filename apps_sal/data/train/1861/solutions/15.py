from collections import defaultdict

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        x_dict = defaultdict(set)
        
        # x coordinate as key, y coordiante as value
        for x, y in points:
            x_dict[x].add(y)
            
        x_vals = list(x_dict.keys())
        best = float(\"inf\")
        
        # loop through combinations
        for i in range(1, len(x_vals)):
            for j in range(i):
                matching_y = []
                
                # find all matching y values, keep track of largest and smallest
                for y in x_dict[x_vals[i]]: 
                    if y in x_dict[x_vals[j]]:
                        matching_y.append(y)
                        
                # if found two distinct matching y values, can make rectangle
                if len(matching_y) >= 2:
                    smallest_diff = get_smallest_diff(matching_y)
                    best = min(best, smallest_diff * abs(x_vals[i] - x_vals[j]))
                
        return 0 if best == float(\"inf\") else best
    
def get_smallest_diff(array):
    array.sort()
    smallest = float(\"inf\")
    
    for i in range(len(array) - 1):
        smallest = min(smallest, array[i + 1] - array[i])
        
    return smallest
