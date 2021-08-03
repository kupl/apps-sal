# cook your dish here
for _ in range(int(input())):
    n = int(input())
    mat = [list(map(int, input().strip().split()))
           for i in range(n)]
    ans = 0
    equal = True
    for i in range(n - 1, 0, -1):
        if equal and mat[0][i] != i + 1:
            ans += 1
            equal = False
        elif not equal and mat[0][i] == i + 1:
            ans += 1
            equal = True
    print(ans)
