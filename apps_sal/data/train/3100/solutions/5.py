def max_and_min(arr1,arr2):
    def mini(i, j):
        if i == len(a1) or j == len(a2):
            return float('inf')
        val = a1[i] - a2[j]
        if val < 0:
            return min(-val, mini(i+1, j))
        return min(val, mini(i, j+1))    
    
    a1, a2 = sorted(arr1), sorted(arr2)
    return [max(a2[-1]-a1[0], a1[-1]-a2[0]), bool(set(a1)^set(a2)) and mini(0, 0)]
