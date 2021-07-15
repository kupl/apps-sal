from queue import Queue

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        memo = {}
        def countMemo(currLocation, currFuel):
            if memo.get((currLocation, currFuel)) is not None:
                return memo.get((currLocation, currFuel))
            else:
                result = 0
                if currLocation == locations[finish]:
                    result = 1
                for l in locations:
                    if currFuel - abs(currLocation - l) >= 0 and l != currLocation:
                        result += countMemo(l, currFuel - abs(currLocation - l))
                memo[(currLocation, currFuel)] = result
                return result
        
        r = countMemo(locations[start], fuel) % ((10 ** 9) + 7)
        #(memo)
        return r
