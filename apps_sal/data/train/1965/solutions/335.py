import bisect
import functools
from typing import List


class Solution:
  def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

    result = 0
    e = [[_, u-1, v -1] for _, u, v in edges]
    a = [i for i in range(n)]
    b = [i for i in range(n)]
    def find(p, x):
      p[x] = p[x] if p[x] == x else find(p, p[x])
      return p[x]

    def union(p, a, b):
      find_a = find(p, a)
      find_b = find(p, b)
      if find_a == find_b:
        return 1
      p[find_a] = find_b
      return 0

    same = 0
    for type, u, v in e:
      if type == 3:
        same += union(a, u, v) | union(b, u, v)

    for type, u, v in e:
      if type == 1:
        same += union(a, u, v)
      if type == 2:
        same += union(b, u, v)

    all_a = all(find(a, 0) == find(a, x) for x in a)
    all_b = all(find(b, 0) == find(b, x) for x in b)
    if all_a and all_b:
      return same

    return -1
