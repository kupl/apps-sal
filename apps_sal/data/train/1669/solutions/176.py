class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if (W == 1):
            return True
        sorted_indexes = []
        frequency_map = {}
        for h in hand:
            if h not in list(frequency_map.keys()):
                frequency_map[h] = 1
                self.addToSortedList(h, sorted_indexes)
            else:
                frequency_map[h] += 1

        print((sorted_indexes, frequency_map))
        index = 0
        while index < len(sorted_indexes):
            for ele in range(sorted_indexes[index], sorted_indexes[index] + W):
                if ele not in list(frequency_map.keys()) or frequency_map[ele] == 0:
                    return False

                frequency_map[ele] -= 1
            while (index < len(sorted_indexes) and frequency_map[sorted_indexes[index]] == 0):
                frequency_map.pop(sorted_indexes[index])
                index += 1

        return len(list(frequency_map.keys())) == 0

    def addToSortedList(self, value: int, sorted_list: List[int]):
        if (len(sorted_list) == 0):
            sorted_list.append(value)
            return
        low = 0
        high = len(sorted_list) - 1
        while (low < high):
            mid = math.floor((low + high) / 2)
            if value < sorted_list[mid]:
                high = mid - 1
            elif value > sorted_list[mid]:
                low = mid + 1
        if high < 0:
            sorted_list.insert(0, value)
        elif value > sorted_list[high]:
            sorted_list.insert(high + 1, value)
        else:
            sorted_list.insert(high, value)
