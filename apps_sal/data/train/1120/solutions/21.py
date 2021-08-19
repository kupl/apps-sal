for ii in range(int(input())):
    (r, c) = list(map(int, input().split()))
    (x, y) = list(map(int, input().split()))
    mw = max(abs(y - c + 1), y)
    mh = max(abs(x - r + 1), x)
    print(mw + mh)
' visited = [[False for i in range(c)] for j in range(r)]\n    def traverse(row, col):\n     if not(0 <= row < r):\n      return 0\n     if not(0 <= col < c):\n      return 0\n     if visited[row][col]: return 0\n     a = 0\n     visited[row][col] = True\n     for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:\n      a = max(a, traverse(i+row,j+col))\n     return 1 + a\n    print(traverse(x, y ))\n'
