class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = 0
        for item in target:
            if item not in arr:
                return False
        hash_map_arr = {}
        hash_map_target = {}
        for i in range(len(arr)):
            if arr[i] not in hash_map_arr:
                hash_map_arr[arr[i]] = 1
            else:
                hash_map_arr[arr[i]] += 1
            if target[i] not in hash_map_target:
                hash_map_target[target[i]] = 1
            else:
                hash_map_target[target[i]] += 1
        for item in target:
            if hash_map_arr[item] != hash_map_target[item]:
                return False
        return True
