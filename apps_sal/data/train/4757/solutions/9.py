def solve(n,m,a,b,ans):
    col = 0
    grid = [[0 for j in range(m)] for i in range(n)]
    for row in range(n):
        count = 0
        while count != a:
            grid[row][col] = 1
            col += 1
            count += 1
            if col == m:
                col = 0

    for row in range(n):
        count = 0
        for col in range(m):
            if grid[row][col] == 1:
                count += 1

        if count != a:
            ans.append(['NO'])
            return

    for col in range(m):
        count = 0
        for row in range(n):
            if grid[row][col] == 1:
                count += 1

        if count != b:
            ans.append(['NO'])
            return

    ans.append(['YES'])
    for row in range(n):
        s = ''
        for col in grid[row]:
            s += str(col)

        ans.append([s])

def main():
    t = int(input())
    ans = []
    for i in range(t):
        n,m,a,b = list(map(int,input().split()))
        solve(n,m,a,b,ans)

    for i in ans:
        for j in i:
            print(j)


main()

