n = int(input())
arr = [int(x) for x in input().split()]
m = int(input())
ans = []
while m > 0:
    x = int(input())
    val = arr[x - 1]
    ans.append(val)
    arr.remove(val)
    m -= 1
for x in ans:
    print(x)
