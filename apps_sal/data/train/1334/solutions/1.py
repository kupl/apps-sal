INT_MAX = 1000000000000000000
n = int(input())
ar = list(map(int, input().split()))
br = [0] * 1
br.extend(ar)
del ar
for i in range(n - 3, 0, -1):
    br[i] = min(br[i + 1], br[i + 2], br[i + 3]) + br[i]
print(min(br[1:4]))
