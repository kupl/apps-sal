# cook your dish here
n, m = list(map(int, input().split(" ")))
for i in range(m):
    q = int(input())
    if(q < n + 2):
        print('0')
        continue
    else:
        print(n - abs(2 * n + 1 - q))
