from collections import Counter
class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.min_arr_len = len(arr) // 2
        self.main = Counter(arr)
        self.subarrs = {}
        max_repeats = max(self.main.values())
        max_idx = list(self.main.values()).index(max_repeats)
        self.rets = {(0, len(arr)-1): (max_repeats,
                                       list(self.main.keys())[max_idx])}

    def query(self, left: int, right: int, threshold: int) -> int:
        # check if return value has already been calculated
        if (left, right) in self.rets:
            if self.rets[(left, right)][0] >= threshold:
                print(\"Getting return val from cache...\")
                return self.rets[(left, right)][1]

        targarr = self.arr[left:right+1]
        if len(targarr) > self.min_arr_len:
            # count the new sub-array using main counter
            # this should always be less than O(n)
            self.subarrs[left] = {right: self.main.copy()} 
            if left > 0:
                for num in self.arr[0:left]:
                    self.subarrs[left][right][num] -= 1
            if right < len(self.arr) - 1:
                for num in self.arr[right+1:]:
                    self.subarrs[left][right][num] -= 1
        else:
            # try to create subarray from existing array
            if left in self.subarrs:
                largest = max(self.subarrs[left].keys())
                min_len = ((largest + 1) - left) // 2
                if len(targarr) < (largest+1)-left and len(targarr) > min_len:
                    self.subarrs[left][right] = self.subarrs[left][largest]
                    for num in self.arr[right+1:largest+1]:
                        self.subarrs[left][right][num] -= 1
                else:
                    self.subarrs[left][right] = Counter(targarr)
            else:
                self.subarrs[left] = {right: Counter(targarr)}
            
        # get the most repeated number and the no. of repeats
        subarr_vals = list(self.subarrs[left][right].values())
        max_repeats = max(subarr_vals)
        max_idx = subarr_vals.index(max_repeats)
        repeat_num = list(self.subarrs[left][right].keys())[max_idx]
        # save result
        self.rets[(left, right)] = (max_repeats, repeat_num)
        
        if self.rets[(left, right)][0] >= threshold:
            return self.rets[(left, right)][1]
        
        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
