for ii in range(int(input())):
    r, c = list(map(int, input().split()))
    x, y = list(map(int, input().split()))
    mw = max(abs(y - c + 1), y)
    mh = max(abs(x - r + 1), x)
    #print("diff ", abs(x-c+1))
    # print(mw,mh)
    print(mw + mh)
''' visited = [[False for i in range(c)] for j in range(r)]
    def traverse(row, col):
     if not(0 <= row < r):
      return 0
     if not(0 <= col < c):
      return 0
     if visited[row][col]: return 0
     a = 0
     visited[row][col] = True
     for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
      a = max(a, traverse(i+row,j+col))
     return 1 + a
    print(traverse(x, y ))
'''
