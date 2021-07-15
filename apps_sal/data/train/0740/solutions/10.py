# cook your dish here
def fence(n, m, k, coords):
 # def bfs(n, m, s, visited):
 #   from collections import deque
 #   q = deque([s])
 #   visited.add(s)
 #   dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
 #   f = 0
 #   while q:
 #       sr, sc = q.popleft()
 #       for dr, dc in dirs:
 #           new_sr, new_sc = sr+dr, sc+dc
 #           new_s = (new_sr, new_sc)
 #           if new_sr >= 0 and new_sr < n and \
 #           new_sc >= 0 and new_sc < m and new_s not in visited: 
 #               q.append(new_s); visited.add(new_s)
 #           else: f += 1
 #   return f
 # r, visited = 0, set([])
 # for s in coords:
 #   if s not in visited:
 #       r += bfs(n, m, s, visited)
 # return r
 dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
 f = 0
 for coord in coords:
  for dx, dy in dirs:
   x, y = coord[0]+dx, coord[1]+dy
   if x >= 0 and x < n and y >= 0 and y < m and (x, y) in coords:
    pass
   else:
    f += 1
 return f
 
t = int(input())
for _ in range(t):
 n, m, k = map(int, input().split())
 L = []
 for _ in range(k):
  a, b = map(int, input().split())
  L.append((a-1, b-1))
 coords = set(L)
 print(fence(n, m, k, coords))
