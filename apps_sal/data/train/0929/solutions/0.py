# cook your dish here
import numpy as np
tests = int(input())
for _ in range(tests):
   n = int(input())
   weights = [int(j) for j in input().split()]
   edges = [[0] for _ in range(n-1)]
   for i in range(n-1):
      edges[i] = [int(j)-1 for j in input().split()]
   vertex_set = [[] for _ in range(n)]
   for i in range(n-1):
      vertex_set[edges[i][0]].append(edges[i][1])
      vertex_set[edges[i][1]].append(edges[i][0])
   counts = [0 for _ in range(3)]
   for i in range(n):
      counts[weights[i]] += 1
   if counts[1] == 0:
      print(2 * (counts[0] != 0 and counts[2] != 0))
   elif counts[1] == n:
      print(0)
   else:
      visited = [0]
      for i in range(n):
         vertex = visited[i]
         for v in vertex_set[vertex]:
            if v not in visited:
               visited.append(v)
      vertex_nums = [[0] for _ in range(n)]
      for i in range(n-1,-1,-1):
         vertex = visited[i]
         for v in vertex_set[vertex]:
            if v in visited[i:]:
               vertex_nums[vertex].append(sum(vertex_nums[v])+1)
      for i in range(n):
         vertex_nums[i].append(n-1-sum(vertex_nums[i]))
      sums = np.zeros(n,dtype=bool)
      sums[0] = True
      for i in range(n):
         new_sums = np.zeros(n,dtype=bool)
         new_sums[0] = True
         for num in vertex_nums[i]:
            new_sums[num:n] = np.logical_or(new_sums[num:n],new_sums[:n-num])
         sums = np.logical_or(sums,new_sums)
      solved = False
      for i in range(n):
         if sums[i] and counts[0] <= i and counts[2] <= n - 1 - i:
            solved = True
            break
      if solved or counts[1] > 1:
         print(1)
      else:
         print(2)
