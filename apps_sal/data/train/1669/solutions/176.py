class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        # Q: repititions allowed? yes 
        # Q: negative numbers allowed? no 
        # brute force: make a hashmap with the key as hand[i] and value as frequency: O(n)
        # maintain a sorted list of indexes: O(n*log(n))
        # make a pass over the sorted list of indexes, and move to next when the frequency goes to 0 -> O(n)
        # time complexity = O(n*log(n))
        if (W==1):
            return True 
        sorted_indexes = []
        frequency_map = {}
        for h in hand: 
            if h not in list(frequency_map.keys()):
                frequency_map[h] = 1
                # add to sorted list 
                self.addToSortedList(h, sorted_indexes)       
            else: 
                frequency_map[h] += 1
                
        print((sorted_indexes, frequency_map))
        # using frequency_map, and sorted_indexes, check if consecutive lists can be made 
        index = 0
        while index < len(sorted_indexes):
            # start the current W length list with sorted_indexes[index]        
            for ele in range(sorted_indexes[index], sorted_indexes[index]+W):
                if ele not in list(frequency_map.keys()) or frequency_map[ele] == 0:
                    return False
                
                frequency_map[ele] -= 1
            while (index < len(sorted_indexes) and frequency_map[sorted_indexes[index]] == 0):
                # remove the element from frequency_map
                frequency_map.pop(sorted_indexes[index])
                index += 1
                
        return len(list(frequency_map.keys())) == 0 
        
    def addToSortedList(self, value: int, sorted_list: List[int]):
        # values are not repeated in the sorted list 
        if (len(sorted_list) == 0):
            sorted_list.append(value)
            return
        #print(\"---> val:\" + str(value))
        low = 0 
        high = len(sorted_list) - 1
        while (low < high):
            mid = math.floor((low+high)/2)
            #print(mid, low, high)
            if value < sorted_list[mid]:
                high = mid - 1
            elif value > sorted_list[mid]:
                low = mid + 1
        #print(value, low, high, sorted_list)
        if high < 0:
            sorted_list.insert(0, value)
        elif value > sorted_list[high]:
            sorted_list.insert(high+1, value)
        else:
            sorted_list.insert(high, value)

