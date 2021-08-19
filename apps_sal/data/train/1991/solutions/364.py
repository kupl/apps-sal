import collections


class Solution:

    def countRoutes(self, locations, start: int, finish: int, fuel: int) -> int:
        self.memorization = collections.defaultdict(int)

        def dfs_memorization(index, currentCityValue, destinationIndex, remainingFuel, locations):
            temp_count = 0
            if (index, currentCityValue, remainingFuel) in self.memorization:
                return self.memorization[index, currentCityValue, remainingFuel]
            if remainingFuel < 0:
                self.memorization[index, currentCityValue, remainingFuel] = 0
                return 0
            if remainingFuel == 0 and index == destinationIndex:
                self.memorization[index, currentCityValue, remainingFuel] = 1
                return 1
            if remainingFuel == 0 and index != destinationIndex:
                self.memorization[index, currentCityValue, remainingFuel] = 0
                return 0
            if index == destinationIndex:
                temp_count += 1
            for i in range(len(locations)):
                if i == index:
                    continue
                temp_count += dfs_memorization(i, locations[i], destinationIndex, remainingFuel - abs(currentCityValue - locations[i]), locations)
            self.memorization[index, currentCityValue, remainingFuel] = temp_count
            return temp_count
        count = dfs_memorization(start, locations[start], finish, fuel, locations)
        return count % (10 ** 9 + 7)
