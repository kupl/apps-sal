class Solution:
\tdef maxNumEdgesToRemove(self, n: int, edges: [[int]]) -> int:
\t\tdef find(arr: [int], x: int) -> int: 
\t\t\tif arr[x] != x:
\t\t\t\tarr[x] = find(arr, arr[x])
\t\t\treturn arr[x]

\t\tdef union(arr: [int], x: int, y: int) -> int:
\t\t\tpx, py = find(arr, x), find(arr, y)
\t\t\tif px == py:
\t\t\t\treturn 0
\t\t\tarr[px] = py
\t\t\treturn 1

\t\tarr = [i for i in range(n+1)]
\t\ta, b, ans = 0, 0, 0
\t\tfor t, x, y in edges:
\t\t\tif t == 3:
\t\t\t\tif union(arr, x, y):
\t\t\t\t\ta += 1
\t\t\t\t\tb += 1
\t\t\t\telse:
\t\t\t\t\tans += 1

\t\ttmp = arr[:]
\t\tfor t, x, y in edges:
\t\t\tif t == 1:
\t\t\t\tif union(arr, x, y):
\t\t\t\t\ta += 1
\t\t\t\telse:
\t\t\t\t\tans += 1

\t\tarr = tmp
\t\tfor t, x, y in edges:
\t\t\tif t == 2:
\t\t\t\tif union(arr, x, y):
\t\t\t\t\tb += 1
\t\t\t\telse:
\t\t\t\t\tans += 1

\t\treturn ans if a == b == n-1 else -1
