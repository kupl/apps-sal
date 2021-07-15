class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
      milesDict = {}

      for trip in trips:
        passengers = trip[0]
        start = trip[1]
        end = trip[2]

        mile = start

        while mile < end:
          if mile in milesDict:
            milesDict[mile] = milesDict[mile] + passengers
          else:
            milesDict[mile] = passengers

          mile = mile + 1

      if max(milesDict.values()) <= capacity:
        return True
      else:
        return False

