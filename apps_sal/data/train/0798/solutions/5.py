N, M = map(int,input().split())
grid = [[int(i) for i in input().split()]for j in range(N)]
charms = [[*map(int,input().split())] for i in range(M)]
 
dp = [[None for n in range(N)] for m in range(N)]
 
dp[0][0] = grid[0][0] # Base case
 
def valid_square(coord, charms):
    # Checks to see if a square is valid
    for charm in charms:
        if abs(coord[0]+1 - charm[0])+abs(coord[1]+1 - charm[1]) <= charm[2]:
            return True
    return False
 
for y in range(N):
    for x in range(N):
        if valid_square((y,x), charms):
            if y == 0:
                if dp[y][x-1]:
                    dp[y][x] = dp[y][x-1] + grid[y][x]
            elif x == 0:
                if dp[y-1][x]:
                    dp[y][x] = dp[y-1][x] + grid[y][x]
            else:
                if dp[y-1][x] or dp[y][x-1]:
                    dp[y][x] = grid[y][x]+max(dp[y][x-1]or 0,dp[y-1][x]or 0)
if dp[N-1][N-1]:
    print("YES")
    print(dp[N-1][N-1])
else:
    print("NO")
