# cook your dish here
n = int(input())
arr = [int(s) for s in input().split(" ")]
ans = []
for x in arr:
    if x == 2:
        ans.append(1)
    else:
        ans.append(x^2)
print(*ans)
