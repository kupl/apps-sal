def recursive_dfs(graph, start, path=[]):
  '''recursive depth first search from start'''
  path=path+[start]
  for node in graph[start]:
    if not node in path:
      path=recursive_dfs(graph, node, path)
  return path

def connected(x, y):
    if set(x).intersection(set(y)) != set():
        return True
    return False

vertices = []
each = {}
adj = {}
num0 = 0
a, b = list(map(int, input().split(' ')))
for i in range(a):
    x = list(map(int, input().split(' ')))
    adj[i] = []
    if x[0] == 0:
        num0 += 1
    else:
        x = x[1:]
        each[i] = x
        vertices.append(i)

        for j in vertices:
            if connected(each[j], each[i]):
                adj[j].append(i)
                adj[i].append(j)
            
marked = [False] * a
num = 0
for i in vertices:
  if not marked[i]:
    for j in recursive_dfs(adj, i):
      marked[j] = True
    num += 1

if num == 0:
    print(num0)
else:
    print(num+num0-1)

