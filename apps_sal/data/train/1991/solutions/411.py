import numpy
import heapq
import sys

from collections import defaultdict
from typing import List


class Solution:
  def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
    dims = (len(locations), fuel+1)
    dp = numpy.zeros(dims)
    dp[start][fuel] = 1
    module = 10 ** 9 + 7
    for f in range(fuel, 0, -1):
      for city in range(len(locations)):
        if int(dp[city][f]) == 0:
          continue
        if abs(locations[city] - locations[finish]) > f:
          continue
        for j in range(len(locations)):
          distance = abs(locations[j] - locations[city])
          if j == city:
            continue
          if f < distance:
            continue

          dp[j][f - distance] = (dp[j][f - distance] + dp[city][f]) % module

    return int(sum(dp[finish]) % module)
